
import logging
import os
import pickle
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Tuple
from pathlib import Path

import numpy as np
import pandas as pd


class DataReader:
    DATASET_NAME="Fitapp"
    _DATA_PATH = Path(Path.home() / os.environ.get("DATA_PATH"))
    _DATASET_PATH = _DATA_PATH / DATASET_NAME
    base_action=['Squat', 'Plank', 'Push Up', 'Jumping Jacks',  'Bridge / Wheel', 'L-Sit', 'Mountain Climber', 'Burpee', 'Lunge', 'Crunch']
    actions=['Reverse Plank', 'Shoulder Bridge', 'Incline Reverse Plank', 'Declined Shoulder Bridge', 'Single Leg Bridge', 'Declined Single Leg Bridge', 'Table Bridge', 'Inclined Table Bridge', 'Head Bridge', 'Bridge / Wheel', 'Declined Bridge / Wheel', 'Burpee Walk', 'Burpee', 'Squat Burpee', 'Full Burpee', 'Push-Up Jack Burpee', 'Spiderman Burpee', 'Pike Push-Up Burpee', 'Mountain-Climber Burpee', 'Side-Plank Burpee', 'Tuck-Jump Burpee', 'Hollow Hold', 'Heel Taps', 'Crunch', 'Side Crunch', 'Scissor Kick', 'Beetle', 'Bicycle Crunch', 'High Crunch', 'Reverse Crunch', 'Leg Drops', 'Seated Pike Leg Lift', 'Intermediate Seated Pike Leg Lift', 'Upper Body Jumping Jacks', 'Stepping Jumping Jacks', 'Jumping Jacks', 'Seal Jumping Jacks', 'Squat Jumping Jacks', 'Crossover Jumping Jacks', 'Foot Sup L-Sit', 'One Leg L-Sit', 'Tuck L-Sit', 'L-Sit', 'Reverse Lunge', 'Lunge', 'Crossover Lunge', 'Walking lunge', 'Lunge with Leg Raise', 'Tick-tock Lunge', 'Split Lunge Jump', 'Bulgarian Split Lunge', 'Mountain Climber Switch', 'Mountain Climber', 'Running Mountain Climber', 'Spider Mountain Climber', 'Side to side Mountain Climber', 'Diagonal Mountain Climber', 'Semicircle Mountain Climber', 'Jumping Mountain Climber', 'Low Jumping Mountain Climber', 'Side Plank on Knee', 'Knee Plank', 'Incline Knee Plank', 'Decline Knee Plank', 'Side Plank', 'Plank', 'Knee long lever plank', 'Long Lever Plank', 'Plank Jack', 'Plank with Tow Touch', 'Inchworm Plank', 'Up and Down Plank', 'Straddle One Arm Plank', 'One Arm Plank', 'One Arm One Leg Plank', 'Incline One arm one leg plank', 'Decline One arm one leg plank', 'Negative Knee Push Up', 'Knee Push Up', 'Diamond Knee Push Up', 'Inclined Push Up', 'Push Up', 'Declined Push Up', 'Diamond Push Up', 'Pseudo Planche Push Up', 'Negative Pike Push up', 'Pike Push Up', 'Declined Pike Push Up', 'Archer Push Up', 'Assisted Squat', 'Squat', 'Parallel Squat', 'Power Squat Knee Tuck', 'Cossack Squat', 'Split Squat', 'Bulgarian Split Squat', 'Partial Pistol Squat', 'Pistol Squat', 'Beginner Shrimp Squat', 'Int Shrimp Squat']
    def __init__(self) -> None:
        assert self.DATASET_NAME is not None, "Dataset name has not been set"
    def create_dataset(self):   
        dataset=pd.read_csv("user5.csv", sep=",")
        
        ind=[]
        for i in range(0,100):
            ind.append(i)
        action_dict=dict(zip(ind,self.actions))
        dataset['mov']=dataset['mov'].map(action_dict)
        for index,rows in dataset.iterrows():
            k=dataset['hidden_mov'][index].strip('\n')
            k=k.strip('[')
            k=k.strip(']')
            list_1 = k.split()
            dataset['hidden_mov'][index]=list_1
        
        ind1=[]
        for i in range(0,10):
            ind1.append(i)
        base_action_dict=dict(zip(ind1,self.base_action))
        dataset['base_mov']=dataset['base_mov'].map(base_action_dict)
        for index,rows in dataset.iterrows():
            for j in range(100):
                if(float(dataset.hidden_mov[index][j])>0.5):
                    dataset.hidden_mov[index][j]=1
                if((float(dataset.hidden_mov[index][j])> -0.5) & (float(dataset.hidden_mov[index][j])<0.5)):
                    dataset.hidden_mov[index][j]=0
                if(float(dataset.hidden_mov[index][j])< -0.5):
                    dataset.hidden_mov[index][j]=-1
        dataset.to_feather(self._DATASET_PATH)
        print("saved dataset")

    def movements(self):
        actions=self.actions
        return actions
    def base_movements(self):
        actions=self.base_action
        return actions


    def load_dataset(self):
        save_path = self._DATASET_PATH 
        load_path = save_path 
        recs = pd.read_feather(load_path)
        return recs


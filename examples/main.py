import random
import time
import json
from pprint import pprint
import glob

import optuna
import pandas as pd
import matplotlib.pyplot as plt
import joblib

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

from codes.problems.OneMax import OneMax
from codes.problems.EightQueen import EightQueen
from codes.problems.TSP import TSP
from codes.problems.LifeGame import LifeGame
from codes.problems.g2048 import g2048
from codes.problems.function_Ackley import function_Ackley
from codes.problems.function_Griewank import function_Griewank
from codes.problems.function_Michalewicz import function_Michalewicz
from codes.problems.function_Rastrigin import function_Rastrigin
from codes.problems.function_Schwefel import function_Schwefel
from codes.problems.function_StyblinskiTang import function_StyblinskiTang
from codes.problems.function_XinSheYang import function_XinSheYang


from codes.algorithms.GA import GA
from codes.algorithms.PfGA import PfGA
from codes.algorithms.ABC import ABC
from codes.algorithms.Bat import Bat
from codes.algorithms.Cuckoo import Cuckoo
from codes.algorithms.Cuckoo_greedy import Cuckoo_greedy
from codes.algorithms.DE import DE
from codes.algorithms.Firefly import Firefly
from codes.algorithms.Harmony import Harmony
from codes.algorithms.PSO import PSO
from codes.algorithms.WOA import WOA
from codes.algorithms.GA_BLXa import GA_BLXa
from codes.algorithms.Tabu import Tabu


def create_problem(prob_cls):
    if prob_cls.__name__ == OneMax.__name__:
        return OneMax(10000)
    if prob_cls.__name__ == EightQueen.__name__:
        return EightQueen(20)
    if prob_cls.__name__ == TSP.__name__:
        return TSP(80)
    if prob_cls.__name__ == LifeGame.__name__:
        return LifeGame(20, max_turn=5)
    if prob_cls.__name__ == g2048.__name__:
        return g2048(max_turn=350)
    if prob_cls.__name__ == function_Ackley.__name__:
        return function_Ackley(50)
    if prob_cls.__name__ == function_Griewank.__name__:
        return function_Griewank(100)
    if prob_cls.__name__ == function_Michalewicz.__name__:
        return function_Michalewicz(70)
    if prob_cls.__name__ == function_Rastrigin.__name__:
        return function_Rastrigin(70)
    if prob_cls.__name__ == function_Schwefel.__name__:
        return function_Schwefel(50)
    if prob_cls.__name__ == function_StyblinskiTang.__name__:
        return function_StyblinskiTang(80)
    if prob_cls.__name__ == function_XinSheYang.__name__:
        return function_XinSheYang(200)
    raise ValueError()

    

def objective_degree(prob_cls, alg_cls, timeout):
    def objective(trial):
        if alg_cls.__name__ == GA.__name__:
            alg = GA(
                trial.suggest_int('individual_max', 2, 50),
                trial.suggest_categorical('save_elite', [False, True]),
                trial.suggest_categorical('select_method', ["ranking", "roulette"]),
                trial.suggest_uniform('mutation', 0.0, 1.0),
            )
        elif alg_cls.__name__ == PfGA.__name__:
            alg = PfGA(
                trial.suggest_uniform('mutation', 0.0, 1.0),
            )
        elif alg_cls.__name__ == ABC.__name__:
            alg = ABC(
                trial.suggest_int('harvest_bee', 2, 50),
                trial.suggest_int('follow_bee', 1, 100),
                trial.suggest_int('visit_max', 1, 100),
            )
        elif alg_cls.__name__ == Bat.__name__:
            alg = Bat(
                trial.suggest_int('bat_max', 2, 50),
                trial.suggest_uniform('frequency_min', 0, 0),
                trial.suggest_uniform('frequency_max', 0, 1),
                trial.suggest_uniform('good_bat_rate', 0, 1),
                trial.suggest_uniform('volume_init', 0, 2),
                trial.suggest_uniform('volume_update_rate', 0, 1),
                trial.suggest_uniform('pulse_convergence_value', 0, 1),
                trial.suggest_uniform('pulse_convergence_speed', 0, 1),
            )
        elif alg_cls.__name__ == Cuckoo.__name__:
            alg = Cuckoo(
                trial.suggest_int('nest_max', 2, 50),
                trial.suggest_uniform('scaling_rate', 0, 2.0),
                trial.suggest_uniform('levy_rate', 0, 1.0),
                trial.suggest_uniform('bad_nest_rate', 0, 1.0),
            )
        elif alg_cls.__name__ == Cuckoo_greedy.__name__:
            alg = Cuckoo_greedy(
                trial.suggest_int('nest_max', 2, 50),
                trial.suggest_uniform('epsilon', 0, 1.0),
                trial.suggest_uniform('bad_nest_rate', 0, 1.0),
            )
        elif alg_cls.__name__ == DE.__name__:
            alg = DE(
                trial.suggest_int('agent_max', 4, 50),
                trial.suggest_uniform('crossover_rate', 0, 1.0),
                trial.suggest_uniform('scaling', 0, 2.0),
            )
        elif alg_cls.__name__ == Firefly.__name__:
            alg = Firefly(
                trial.suggest_int('firefly_max', 2, 50),
                trial.suggest_uniform('attracting_degree', 0.0, 1.0),
                trial.suggest_uniform('absorb', 0.0, 50.0),
                trial.suggest_uniform('alpha', 0.0, 1.0),
                trial.suggest_categorical('is_normalization', [False, True]),
            )
        elif alg_cls.__name__ == Harmony.__name__:
            alg = Harmony(
                trial.suggest_int('harmony_max', 2, 50),
                trial.suggest_uniform('bandwidth', 0.0, 1.0),
                trial.suggest_categorical('enable_bandwidth_rate', [False, True]),
                trial.suggest_uniform('select_rate', 0.0, 1.0),
                trial.suggest_uniform('change_rate', 0.0, 1.0),
            )
        elif alg_cls.__name__ == PSO.__name__:
            alg = PSO(
                trial.suggest_int('particle_max', 2, 50),
                trial.suggest_uniform('inertia', 0.0, 1.0),
                trial.suggest_uniform('global_acceleration', 0.0, 1.0),
                trial.suggest_uniform('personal_acceleration', 0.0, 1.0),
            )
        elif alg_cls.__name__ == WOA.__name__:
            alg = WOA(
                trial.suggest_int('whale_max', 2, 50),
                trial.suggest_uniform('a_decrease', 0.0, 0.1),
                trial.suggest_uniform('logarithmic_spiral', 0.0, 2.0),
            )
        elif alg_cls.__name__ == GA_BLXa.__name__:
            alg = GA_BLXa(
                trial.suggest_int('individual_max', 2, 50),
                trial.suggest_categorical('save_elite', [False, True]),
                trial.suggest_categorical('select_method', ["ranking", "roulette"]),
                trial.suggest_uniform('mutation', 0.0, 1.0),
                trial.suggest_uniform('blx_a', 0.0, 1.0),
            )
        elif alg_cls.__name__ == Tabu.__name__:
            alg = Tabu(
                trial.suggest_int('individual_max', 2, 50),
                trial.suggest_uniform('epsilon', 0.0, 1.0),
                trial.suggest_int('tabu_list_size', 1, 500),
                trial.suggest_uniform('tabu_range_rate', 0.0, 1.0),
            )
        else:
            raise ValueError

        score, _, _ = run(prob_cls, alg, 999999, timeout)
        return score
    return objective


def run(prob_cls, alg, epochs, timeout):
    prob = create_problem(prob_cls)
    random.seed(1)
    prob.init()
    random.seed()

    alg.init(prob)

    # loop
    t0 = time.time()
    for i in range(epochs):
        if time.time() - t0 > timeout:
            break
        alg.step()

    return alg.getMaxScore(), i, alg.count




def multi_run(params):
    prob_cls = params[0]
    alg_cls = params[1]
    best_params = params[2]

    alg = alg_cls(**best_params)
    max_data, step_count, alg_count = run(prob_cls, alg, 999999, timeout=2)

    return {
        "score": max_data,
        "step_count": step_count,
        "alg_count": alg_count,
    }


def main():
    tmp_dir = os.path.join(os.path.dirname(__file__), '..', 'tmp')
    
    probs = [
        OneMax,
        EightQueen,
        TSP,
        LifeGame,
        g2048,
        function_Ackley,
        function_Griewank,
        function_Michalewicz,
        function_Rastrigin,
        function_Schwefel,
        function_StyblinskiTang,
        function_XinSheYang,
    ]
    algs = [
        GA,
        PfGA,
        ABC,
        Bat,
        Cuckoo,
        Cuckoo_greedy,
        DE,
        Firefly,
        Harmony,
        PSO,
        WOA,
        GA_BLXa,
        Tabu,
    ]

    optuna.logging.disable_default_handler()
    for prob_cls in probs:
        for alg_cls in algs:
            path = os.path.join(tmp_dir, "{}_{}.json".format(prob_cls.__name__, alg_cls.__name__))
            #if os.path.isfile(path):
            #    continue  # すでにデータがある場合はskip

            print("start: {} {}".format(prob_cls.__name__, alg_cls.__name__))
            t0 = time.time()

            study = optuna.create_study(
                storage="sqlite:///" + os.path.join(tmp_dir, "optuna_study.db"),
                direction="maximize",
            )
            study.optimize(objective_degree(prob_cls, alg_cls, timeout=2), n_trials=100, n_jobs=4)
            #print(study.best_params)
            #print(study.best_value)

            #---
            params = (prob_cls, alg_cls, study.best_params)
            data = joblib.Parallel(n_jobs=4, verbose=0)([joblib.delayed(multi_run)(params) for _ in range(100)])

            result = {
                "time": time.time()-t0,
                "prob": prob_cls.__name__,
                "alg": alg_cls.__name__,
                "best_params": study.best_params,
                "best_value": study.best_value,
                "data": data
            }

            # output
            with open(path, "w") as f:
                json.dump(result, f, indent=4)


def view():
    tmp_dir = os.path.join(os.path.dirname(__file__), '..', 'tmp')
    data = []
    for fn in glob.glob(os.path.join(tmp_dir, "*.json")):
        print(fn)
        with open(fn, "r") as f:
            data.append(json.load(f))

    # データ加工
    probs = {}
    algs = {}
    for d in data:
        df = pd.DataFrame(d["data"])
        d["min"] = df["score"].min()
        d["mean"] = df["score"].mean()
        d["max"] = df["score"].max()

        #function_XinSheYangは値がすごく小さいので桁数で比較
        if d["prob"] == "function_XinSheYang":
            d["min"] = -int(str(d["min"]).split("e")[1])
            d["mean"] = -int(str(d["mean"]).split("e")[1])
            d["max"] = -int(str(d["max"]).split("e")[1])

        if d["prob"] not in probs:
            probs[d["prob"]] = []
        probs[d["prob"]].append(d)

        if d["alg"] not in algs:
            algs[d["alg"]] = []
        algs[d["alg"]].append({
            "prob": d["prob"],
            "params": d["best_params"],
        })

    # グラフ化
    for name, prob in probs.items():
        df = pd.DataFrame(prob)

        plt.style.use('ggplot')
        df.plot.bar(x="alg", y=["min", "mean", "max"], title="{}".format(name), xlabel="")
        
        tmp_dir = os.path.join(os.path.dirname(__file__), '..', 'tmp')
        path = os.path.join(tmp_dir, "{}.png".format(name))
        print(path)
        plt.tight_layout()
        plt.savefig(path)
        #plt.show()

    # 表示
    for name, alg2 in algs.items():
        print(name)

        # データ整形
        d = []
        for a in alg2:
            print("{} {}".format(a["prob"], a["params"]))
            d2 = {}
            d2["name"] = a["prob"]
            for k, v in a["params"].items():
                d2[k] = v
            d.append(d2)

        df = pd.DataFrame(d)
        print(df)
    

if __name__ == "__main__":
    main()
    view()





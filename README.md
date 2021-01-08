# 最適化アルゴリズム(主にメタヒューリスティクス)の実装コード
以下Qiita記事の実装コードとなります。
コードの解説については記事を参照してください。

+ [todo]()


# 実装アルゴリズム

+ 遺伝的アルゴリズム(Genetic Algorithm: GA)
+ 人口蜂コロニーアルゴリズム(Artificial Bee Colony: ABC)
+ 粒子群最適化(Particle Swarm Optimization: PSO)
+ ホタルアルゴリズム(Firefly Algorithm)
+ コウモリアルゴリズム(Bat Algorithm)
+ カッコウ探索(Cucko Search)
+ ハーモニーサーチ(Harmony Search)
+ くじらさんアルゴリズム(The Whale Optimization Algorithm: WOA)
+ 差分進化(Differential Evolution: DE)


# 実装問題

+ OneMax問題
+ 巡回セールスマン問題(Traveling Salesman Problem: TSP)
+ エイト・クイーン(Eight Queens)
+ ライフゲーム
+ [最適化アルゴリズムを評価するベンチマーク関数まとめ](https://qiita.com/tomitomi3/items/d4318bf7afbc1c835dda)より
  + Ackley function
  + Griewank function
  + Michalewicz function
  + Rastrigin function
  + Schwefel function
  + Styblinski-Tang function
  + Xin-She Yang function


# Getting started
## 1. pip install
使っているパッケージは以下です。

+ pip install numpy
+ pip install matplotlib
+ pip install joblib
+ pip install pandas
+ pip install optuna


## 2. download
このレポジトリをダウンロードします。

``` bash
> git clone https://github.com/pocokhc/metaheuristics.git
```

## 3. Run the program
examples にいくつか実行例が入っています。

``` bash
> cd metaheuristics/examples

# 全問題と全アルゴリズムに対して探索を実行します
> python main.py

# 1次元と2次元を設定できる問題について、各アルゴリズムの探索過程をgif出力します
> python train_plot.py

# 1次元と2次元を設定できる問題について、結果を画像出力します
> python function_plot.py

# TSPを簡単に探索した結果を出力します
> python plot_TSP.py

# ホタルアルゴリズムのLightIntensity関数調査用
> python plot_Firefly.py

```




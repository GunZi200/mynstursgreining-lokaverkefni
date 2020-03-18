# Mynstursgreining Lokaverkefni

## Áætla líftíma rafhlaðna

Þetta verkefni byggist að miklum hluta á eftirfarandi tveimur greinum: 

- [Towards Data Science: Predicting Battery Lifetime with CNNs](https://towardsdatascience.com/predicting-battery-lifetime-with-cnns-c5e1faeecc8f) 
- [Nature: Data-driven prediction of battery cycle life before capacity degradation](https://www.nature.com/articles/s41560-019-0356-8) 



Gögn (8GB): https://data.matr.io/1/projects/5c48dd2bc625d700019f3204

Github síðan þeirra: https://github.com/rdbraatz/data-driven-prediction-of-battery-cycle-life-before-capacity-degradation

Notum (líklegast):

* Keras: https://keras.io/datasets/
* Tensorflow 2: https://blog.tensorflow.org/

Keras og Tensorflow 2 leyfa eins og er bara Python 3.7 (ég nota 3.7.6, en t.d. 3.8.2 virkar ekki)

## Setup
 - [Tensorflow: Tensorboard](https://www.tensorflow.org/tensorboard) 
 - [Tensorflow: Hyperparameter tuning with HParams](https://www.tensorflow.org/tensorboard/hyperparameter_tuning_with_hparams) 
 - [tf.data: Build TensorFlow input pipelines](https://www.tensorflow.org/guide/data) 
 
 
## Process the data
Tekið úr towards data science greininni.
> 1. Take the voltage range during discharging as the reference instead of time!
> For this cell model, 3.6V and 2.0V always correspond to fully charged and discharged. This range stays constant, even when time doesn’t.
> 2. Interpolate charge and temperature over voltage.
> 3. Resample charge and temperature at 1000 equidistant voltage steps.

## Set up the framework
Hérna setum við upp földunarnetið og skilgreinum vel hvernig við förum að því.

![CNN](https://miro.medium.com/max/1250/0*MY2QgQAqk9oHaCNM)

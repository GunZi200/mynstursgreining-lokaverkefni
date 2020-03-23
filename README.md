# Mynstursgreining Lokaverkefni

## Áætla líftíma rafhlaðna

Þetta verkefni byggist að miklum hluta á eftirfarandi tveimur greinum: 

- [Towards Data Science: Predicting Battery Lifetime with CNNs](https://towardsdatascience.com/predicting-battery-lifetime-with-cnns-c5e1faeecc8f) 
- [Nature: Data-driven prediction of battery cycle life before capacity degradation](https://www.nature.com/articles/s41560-019-0356-8) 



Gögn (8GB): https://data.matr.io/1/projects/5c48dd2bc625d700019f3204

Github síðan þeirra: https://github.com/rdbraatz/data-driven-prediction-of-battery-cycle-life-before-capacity-degradation

Github síðan frá þeim sem skrifuðu Towards Data Science greinina: https://github.com/dsr-18/long-live-the-battery

Notum (líklegast):

* Keras: https://keras.io/datasets/
* Tensorflow 2: https://blog.tensorflow.org/

Keras og Tensorflow 2 leyfa eins og er bara Python 3.7 (ég nota 3.7.6, en t.d. 3.8.2 virkar ekki)

## Uppsetning
 - [Tensorflow: Tensorboard](https://www.tensorflow.org/tensorboard) 
 - [Tensorflow: Hyperparameter tuning with HParams](https://www.tensorflow.org/tensorboard/hyperparameter_tuning_with_hparams) 
 - [tf.data: Build TensorFlow input pipelines](https://www.tensorflow.org/guide/data) 
 
## Skilningur á gögnum

Nefna hérna hverskonar gögn eru inn í mælingum. Hvernig er þeim skipt upp.

Hver rafhlaða er tæmd og hlöðuð þangað til að rýmdin hefur minnkað niður í 80% miðað við upphaflegu rýmd. 
 
## Meðhöndlun gagna
Tekið úr towards data science greininni.
> 1. Take the voltage range during discharging as the reference instead of time!
> For this cell model, 3.6V and 2.0V always correspond to fully charged and discharged. This range stays constant, even when time doesn’t.
> 2. Interpolate charge and temperature over voltage.
> 3. Resample charge and temperature at 1000 equidistant voltage steps.

## Set up the framework
tf.Keras using the [functional API](https://www.tensorflow.org/guide/keras/functional). 



## Þróa líkanið
Hérna setum við upp földunarnetið og skilgreinum vel hvernig við förum að því.

Höfundurinn hjá Towards Data Science notar hugtakið *window* mikið hérna. Hvað er *window*?:
> we took multiple consecutive charging cycles as input. These groups of cycles we call **windows**.

Gögnin eru skipt í tvo hluta. Array features og Scalar features.

**Array features:**
1. window size, length, number of features
2. Þessu er hent inn í 3 Conv2D lög með Max Pooling.
3. Síðan er útkoman *Flattened* í 1D fylki.

**Scalar features:**
1. window size, number of features
2. 2 Conv1D lög með einu Max pooling lagi í endan.
3. Síðan er útkoman *Flattened* í 1D fylki.

Þegar það er búið að fletja bæði, þá getum við sameinað gögnin og gert eitthvað með þau.

![CNN](https://miro.medium.com/max/1250/0*MY2QgQAqk9oHaCNM)

* Hvað er max pooling?: https://computersciencewiki.org/index.php/Max-pooling_/_Pooling

## Train and tune the model

Hérna notar Toward Data Science Google Cloud en ég held að það sé of dýrt fyrir okkur. Það þarf aðra lausn.

### Google Cloud AI Platform:
*  [Technical Overview](https://cloud.google.com/ai-platform/docs/technical-overview) 
*  [Getting started: Training and Prediction with Keras](https://cloud.google.com/ai-platform/docs/getting-started-keras)
*  [Getting started: Training and Prediction with TensorFlow Estimator](https://cloud.google.com/ai-platform/docs/getting-started-tensorflow-estimator) 


# Paper: A Review of Video Object Detection: Datasets, Metrics and Methods

## 1. Introduction

Although there are well established object detection methods based on static images,
their application to video data on a frame by frame basis faces two shortcomings:

1. lack of computational effiency due to redundancy across image frames or by not using a temporal and spatial correlation of features across image frames;

2. lack of robustness to real-world conditions such as motion blur and occlusion.


### History of Object Detection for Video Data

In 2015, video object detection became a new task of the ImageNet Large ScaleVisual Recognition Challenge (ILSVRC2015) [5]. With the help of ILSVRC2015, studies in video object detection have further increased.

Earlier attempts in video object detection involved performing object detection on each image frame.

However, using object detection on each image frame does not take into consideration the following attributes in video data:

* Since there exist both *spatial and temporal correlations 空间和时间相关性* between image frames, there are feature extraction redundancies between adjacent frames. Detecting features in each frame leads to computational in-effiency.

* In a long video stream, some frames may have poor quality due to motion blur, video defocus, occlusion, and pose changes. Detecting objects from poor quality frames leads to low accuracies.

Video object detection approaches attempt to address the above challenges. Some approaches **make use of the spatial-temporal information** to improve accuracy, such as fusing features on different levels, e.g., [22–25]. Some other approaches focus on **reducing information redundancy** and improving detection efficiency, e.g., [26–28].

Initially, video object detection approaches have relied on **handcrafted features**, e.g., [29–42]. With the rapid development of deep learning and convolutional neural networks, deep learning models have been shown to be more effective than conventional approaches for various tasks in computer vision [43–50], speech processing [51–55], and multi-modality signal processing [56–61]. A number of deep learning-based video object detection approaches were developed after the ILSVRC2015 challenge. The training is normally done offline. The testing phase on modern GPUs even of complex networks has been shown to meet the 30 frames per sec rate of video, e.g., [26], allowing the real-time deployment of networks.

**The great value of video object detection approaches** is further presented in some specific applications. For example, **hand segmentation** [62,63] is well realized with the help of the optical flow to enhance the feature maps as per the video object detection method [28]. **Human pose estimation** in videos [64] is another successful application, which draws lessons from [22,28] to **solve the motion blur, occlusion and other specific challenges** occurring in videos. Furthermore, **instance-level human parsing** [65] starts from the similar approaches. **Mutual assistance of tracking and detection** [26] is well employed in multiple people tracking [66].

**Deep learning-based video object detection approaches** can be divided into:
  * flow based [22,27,28,67–69]
  * LSTM (Long Short Term Memory)-based [70–73]
  * attention-based [25,74–77]
  * tracking-based [26,78–82] and other methods [36,83–90].
 
## 2. Datasets and Evaluation Metrics

### Datasets

* ImageNet VID dataset [5] (The most commonly used dataset)

  - The dataset is split into a **training set** and a **validation set**, containing **3862** video snippets and **555** video snippets, respectively.
  
  - The video streams are **annotated** on each frame at the frame rate of 25 or 30 fps. 
  
  - In addition, this dataset contains **30 object categories**, which are a subset of the categories in the ImageNet DET dataset [93].

**In the ImageNet VID dataset, the number of objects in each frame is small compared with the datasets used for static image object detection such as COCO [92].**

* EPIC KITCHENS[95]

In 2018, a dataset named EPIC KITCHENS was provided in [95], which consists of **32 different kitchens** in **4 cities** with **11,500,000 frames** containing **454,158 bounding boxes** spanning **290 classes**. However, its kitchen scenario poses limitations on performing generic video object detection.

* Other Datasets:

  - DAVIS dataset [96] for **object segmentation**

  - CDnet2014 [97] for **moving object detection**

  - VOT [98] and MOT [99] for **object tracking**

  - Sports-1M data set [100] with **segment-level annotations**

  - HMDB-51 data set [101] with **segment-level annotations for various human action categories**

  - TRECVID [102] for **video retrieval and indexing**

  - Caltech Pedestrian Detection data set [103] for **pedestrian detection**

  - PASCALVOC dataset [104,105] for **object detection**

  - In addition, some works based on **semi-supervised** or **unsupervised methods** have been considered in [106–109].

*For video object detection with classification labels and tight bounding boxes annotation, currently there exists no public domain dataset offering dense annotations for various complex scenes. To enable the advancement of video object detection, more effort is thus needed to establish comprehensive datasets.*


### Evaluation Metrics

The **metric mean Average Precision (mAP)** is extensively used in conventional object detection, which provides a performance evaluation in terms of regression and classification accuracies [9–15,17]. The evaluation metric **mAP** represents the mean Average Precision. **The definition is the mean of the Average Precision of each category.** As per the PASCAL Visual Object Classes Challenge 2012 (VOC2012) Development Kit, it is computed as follows:

1. The Precision/Recall curve is obtained first. For the Recall (r), the Precision is set to the maximum Precision achieved for any Recall r' ≥ r.

2. The **area under the Precision/Recall curve** is considered to be the Average Precision (AP). The mean of AP in each category is mAP.

## 3. Video Object Detecion Methods

For Video Object Detection, in order to make full use of the video characteristics, different methods are considered to **capture the temporal–spatial relationship**. Some papers have considered the **traditional methods**[29–42]. These papers heavily rely on the manual design leading to the shortcoming of low accuracy and the lack of robustnese to noise sources. **More recently, deep learning solutions have attempted to overcome these shortcomings.** Please see below ppicture:



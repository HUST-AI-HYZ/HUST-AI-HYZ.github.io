---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

# ℹ️ Short Bio

Hi, I'm Yuanzhe, a master student at University of Califronia, San Diego. I have the great honor of being collaborating with [Prof. Yaoqing Yang](https://sites.google.com/site/yangyaoqingcmu/), Prof. [Julian McAuley](https://cseweb.ucsd.edu/~jmcauley/) and Prof. [Zhiting Hu](https://zhiting.ucsd.edu). 

My current research is focused on

- Understanding the mechanisms, dynamics and generalization of LLM and SciML Models [2,3,4].
- Memory mechanisms in LLM & Agent [1,5].

I am actively seeking for <span style="color: red;">**26 Fall CS/ECE PhD Positions**</span>, **research internship** after M.S graduation (about six months), and **collobration opportunities**. 

# 📖 Educations

- *2024.09 - 2026.03 (Expected)*, M.S. in Computer Science and Engineering, University of Califronia, San Diego (UCSD). 
- *2020.09 - 2024.06*, B.S. in Artificial Intelligence, Innovation Experimental Honor Class, Qiming School, Huazhong University of Science and Technology (HUST). GPA: 3.91/4.0. 


# 🔥 News
- *2025.05*: 🎉🎉 Two papers are accepted by [ICML 2025](https://icml.cc/) as **Poster**! See you at Vancouver.
- *2024.09*: &nbsp;🎉🎉 Excited to share that our work “Model Balancing Helps Low-data Training and Fine-tuning” is accepted by [EMNLP 2024](https://2024.emnlp.org) as **Oral Presentation**!
- *2024.06*: &nbsp;😁 I graduated from HUST!
- *2024.06*: &nbsp;😄 I created my account on OpenReview!


# 📝 Writing Samples 

（# denotes equal contribution）

## Under Review & Preprints
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Under Review</div><img src='images/paper_main/MemAgentBench.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**[1] Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions**

{**Yuanzhe Hu#**, Yu Wang#}, Julian McAuley

[Paper](https://openreview.net/pdf?id=ZgQ0t3zYTQ)

Submitted to **NeurIPs 2025 (D&B)** / Will be presented on **ICML 2025 LCFM Workshop**

<!-- TLDR: xxxx -->

</div>
</div>



<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Under Review</div><img src='images/paper_main/Sciml_Diagnosis.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**[2] Loss Landscape Analysis of Scientific Machine Learning Models**

{Haiquan Lu#, **Yuanzhe Hu#**}, Yefan Zhou, Tianyu Pang, Xiaotian Liu, Pu Ren, Yaoqing Yang 

Under Review

</div>
</div>




## Published
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICML 2025</div><img src='images/paper_main/ICML2025_FARMS.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**[3] Eigenspectrum Analysis of Neural Networks without Aspect Ratio Bias**

**Yuanzhe Hu**, Kinshuk Goel, Vlad Killiakov, Yaoqing Yang

[Code](https://github.com/HUST-AI-HYZ/FARMS) \|[Paper](https://arxiv.org/abs/2506.06280) \|[Video](https://recorder-v3.slideslive.com/?share=101775&s=d33c2fb4-ab78-47fc-a76b-0a9e7aef1a02) \|[Review](https://openreview.net/forum?id=7ywj1B3DuO&referrer=%5BAuthor%20Console%5D(%2Fgroup%3Fid%3DICML.cc%2F2025%2FConference%2FAuthors%23your-submissions)) \| ![Star Count](https://img.shields.io/github/stars/HUST-AI-HYZ/FARMS.svg)

**ICML 2025**

</div>
</div>



<div class='paper-box'><div class='paper-box-image'><div><div class="badge">EMNLP 2024</div><img src='images/paper_main/EMNLP_2024.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**[4] Model Balancing Helps Low-data Training and Fine-tuning**

{Zihang Liu#, **Yuanzhe Hu#**}, Tianyu Pang, Yefan Zhou, Pu Ren, Yaoqing Yang

[Code](https://github.com/ZihangHLiu/ModelBalancing) \|[Paper](https://arxiv.org/abs/2410.12178) \|[Video](https://us06web.zoom.us/rec/play/5RHeJiEVuG-yw_Ytt9cHPMzqEIm2xWenwjhHjJ4yt7camtmQObTndJ56YgBBw0A1TlNRGiwZ2MAw5klz.7Xm2WgzcHdxPjGqm?autoplay=true) \|[Review](./pdf/paper_review/Model_balancing_review.pdf) \| ![Star Count](https://img.shields.io/github/stars/ZihangHLiu/ModelBalancing.svg)

**EMNLP 2024 <span style="color: red;">Oral, Rate (168/6105=2.75%)</span>**

</div>
</div>





<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICML 2025</div><img src='images/paper_main/ICML2025_Mplus.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**[5] M+: Extending MemoryLLM with Scalable Long-Term Memory**

Yu Wang, Dmitry Krotov, **Yuanzhe Hu**, Yifan Gao, Wangchunshu Zhou, Julian McAuley, Dan Gutfreund, Rogerio Feris, Zexue He

[HF Model](https://huggingface.co/YuWangX/mplus-8b) \|[Code](https://github.com/wangyu-ustc/MemoryLLM) \|[Paper](https://arxiv.org/abs/2502.00592) \|[Review](https://openreview.net/forum?id=OcqbkROe8J&referrer=%5BAuthor%20Console%5D(%2Fgroup%3Fid%3DICML.cc%2F2025%2FConference%2FAuthors%23your-submissions)) \| ![Star Count](https://img.shields.io/github/stars/wangyu-ustc/MemoryLLM.svg)



**ICML 2025**

</div>
</div>




Last Update: 07/04/2025


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

Hi, I'm Yuanzhe, a master student at University of Califronia, San Diego. I have the great honor of being collaborating with Prof. [Yaoqing Yang](https://sites.google.com/site/yangyaoqingcmu/), Prof. [Julian McAuley](https://cseweb.ucsd.edu/~jmcauley/), Prof. [Zhiting Hu](https://zhiting.ucsd.edu) and Dr. [Ren Pu](https://paulpuren.github.io). 

My current research is focused on

- Understanding the mechanisms, dynamics and generalization of LLM and SciML models via numerical analysis. [2, [3](https://arxiv.org/abs/2506.06280), [4](https://arxiv.org/abs/2410.12178)].
- Memory system in LLM & Agent [[1](https://arxiv.org/abs/2507.05257), [5](https://arxiv.org/abs/2502.00592)].

<!-- I am actively seeking for <span style="color: red;">**26 Fall CS/ECE PhD Positions**</span>, **research internship** after M.S graduation (about six months), and **collobration opportunities**.  -->

# 📖 Educations

<!-- - M.S. in Computer Science and Engineering, University of Califronia, San Diego (UCSD)  &nbsp;  *2024.09 - 2026.03 (Expected)*. 
- *2020.09 - 2024.06*, B.S. in Artificial Intelligence, Innovation Experimental Honor Class, Qiming School, Huazhong University of Science and Technology (HUST). GPA: 3.91/4.0.  -->
<table>
  <tr>
    <td style="width: 60px; border: none; padding: 10px 15px 10px 0;">
      <img src="./images/ucsd_badge.png" width="80">
    </td>
    <td style="border: none; vertical-align: middle;">
      <b>University of California, San Diego (UCSD)</b><br>
      M.S. in Computer Science and Engineering
    </td>
    <td style="text-align: right; border: none; vertical-align: middle; white-space: nowrap;">
      <i>2024.09 - 2026.03 (Expected)</i>
    </td>
  </tr>
  <tr>
    <td style="width: 60px; border: none; padding: 10px 15px 10px 0;">
      <img src="./images/hust_badge.png" width="80">
    </td>
    <td style="border: none; vertical-align: middle;">
      <b>Huazhong University of Science and Technology (HUST)</b><br>
      BEng. in Artificial Intelligence, Innovation Experimental Honor Class, Qiming School<br>
      GPA: 3.91/4.0
    </td>
    <td style="text-align: right; border: none; vertical-align: middle; white-space: nowrap;">
      <i>2020.09 - 2024.06</i>
    </td>
  </tr>
</table>


# 🔥 News
- *2025.07*: &nbsp;😁 We open-sourced the [MemoryAgentBench](https://github.com/HUST-AI-HYZ/MemoryAgentBench). Thanks for the great help from [Yu Wang](https://yuwang.us)! 
- *2025.05*: &nbsp;🎉🎉 Two papers are accepted by [ICML 2025](https://icml.cc/) as **Poster**! See you at Vancouver.
- *2024.09*: &nbsp;🎉🎉 Excited to share that our work “Model Balancing Helps Low-data Training and Fine-tuning” is accepted by [EMNLP 2024](https://2024.emnlp.org) as **Oral Presentation**!
- *2024.06*: &nbsp;😁 I graduated from HUST!
- *2024.06*: &nbsp;😄 I created my account on OpenReview!


# 📝 Writing Samples 

(# denotes equal contribution)

## Preprints & On-Working Prj
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Under Review</div><img src='images/paper_main/MemAgentBench.png' alt="sym" width="80%"></div></div>
<div class='paper-box-text' markdown="1">

**[1] Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions**

{**Yuanzhe Hu#**, Yu Wang#}, Julian McAuley

[HF Dataset](https://huggingface.co/datasets/ai-hyz/MemoryAgentBench) \| [Code](https://github.com/HUST-AI-HYZ/MemoryAgentBench) \| [Paper](https://arxiv.org/abs/2507.05257) \| ![Star Count](https://img.shields.io/github/stars/HUST-AI-HYZ/MemoryAgentBench.svg)

Submitted to **NeurIPs 2025 (D&B)** / **ICML 2025 LCFM Workshop**

</div>
</div>



<div class='paper-box'><div class='paper-box-image'><div><div class="badge">On-Working</div><img src='images/paper_main/Sciml_Diagnosis.jpg' alt="sym" width="80%"></div></div>
<div class='paper-box-text' markdown="1">

**[2] Loss Landscape Analysis of Scientific Machine Learning Models**

<!-- {Haiquan Lu#, **Yuanzhe Hu#**}, Yefan Zhou, Tianyu Pang, Xiaotian Liu, Pu Ren, Yaoqing Yang  -->

On-Working, aimming at ICLR 2026.

</div>
</div>




## Published
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICML 2025</div><img src='images/paper_main/ICML2025_FARMS.jpg' alt="sym" width="80%"></div></div>
<div class='paper-box-text' markdown="1">

**[3] Eigenspectrum Analysis of Neural Networks without Aspect Ratio Bias**

**Yuanzhe Hu**, Kinshuk Goel, Vlad Killiakov, Yaoqing Yang

[Code](https://github.com/HUST-AI-HYZ/FARMS) \| [Paper](https://arxiv.org/abs/2506.06280) \| [ICML Website](https://icml.cc/virtual/2025/poster/46300) \| [Review](https://openreview.net/forum?id=7ywj1B3DuO&referrer=%5BAuthor%20Console%5D(%2Fgroup%3Fid%3DICML.cc%2F2025%2FConference%2FAuthors%23your-submissions)) \| ![Star Count](https://img.shields.io/github/stars/HUST-AI-HYZ/FARMS.svg)

**ICML 2025**

</div>
</div>



<div class='paper-box'><div class='paper-box-image'><div><div class="badge">EMNLP 2024</div><img src='images/paper_main/EMNLP_2024.png' alt="sym" width="80%"></div></div>
<div class='paper-box-text' markdown="1">

**[4] Model Balancing Helps Low-data Training and Fine-tuning**

{Zihang Liu#, **Yuanzhe Hu#**}, Tianyu Pang, Yefan Zhou, Pu Ren, Yaoqing Yang

[Code](https://github.com/ZihangHLiu/ModelBalancing) \| [Paper](https://arxiv.org/abs/2410.12178) \| [Video](https://us06web.zoom.us/rec/play/5RHeJiEVuG-yw_Ytt9cHPMzqEIm2xWenwjhHjJ4yt7camtmQObTndJ56YgBBw0A1TlNRGiwZ2MAw5klz.7Xm2WgzcHdxPjGqm?autoplay=true) \| [Review](./pdf/paper_review/Model_balancing_review.pdf) \| ![Star Count](https://img.shields.io/github/stars/ZihangHLiu/ModelBalancing.svg)

**EMNLP 2024 <span style="color: red;">Oral, Rate (168/6105=2.75%)</span>**

</div>
</div>





<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICML 2025</div><img src='images/paper_main/ICML2025_Mplus.jpg' alt="sym" width="80%"></div></div>
<div class='paper-box-text' markdown="1">

**[5] M+: Extending MemoryLLM with Scalable Long-Term Memory**

Yu Wang, Dmitry Krotov, **Yuanzhe Hu**, Yifan Gao, Wangchunshu Zhou, Julian McAuley, Dan Gutfreund, Rogerio Feris, Zexue He

[机器之心](https://mp.weixin.qq.com/s/8fl3ymmJMn2P0_XBmVQQuw) \| [HF Model](https://huggingface.co/YuWangX/mplus-8b) \| [Code](https://github.com/wangyu-ustc/MemoryLLM) \| [Paper](https://arxiv.org/abs/2502.00592) \| [Review](https://openreview.net/forum?id=OcqbkROe8J&referrer=%5BAuthor%20Console%5D(%2Fgroup%3Fid%3DICML.cc%2F2025%2FConference%2FAuthors%23your-submissions)) \| ![Star Count](https://img.shields.io/github/stars/wangyu-ustc/MemoryLLM.svg)



**ICML 2025**

</div>
</div>




Last Update: 07/2025


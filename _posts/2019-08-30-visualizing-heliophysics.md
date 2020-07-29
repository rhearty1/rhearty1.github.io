---
layout: post
title: Visualizing the intellectual network of heliophysics
categories: [coding]
tags: [history, heliophysics]
---

Here is a heliophysics community to investigate using co-citation analysis. Nodes represent articles and edges connect articles that were cited together in more than three other articles between 1960 and 2010.

![](/assets/heliophysics-co-citation.svg)  

My procedure:
1. I started with a list of 209 living (or recently deceased) scientists who contributed to solar physics.
2. I used Web of Science to generate 5,742 articles co-authored by these scientists, then down-selected the top 1,000 most cited articles from the period 1960 to 2010.
3. I used [Sci2 Tool](https://sci2.cns.iu.edu/user/index.php) and [this tutorial](http://scottbot.net/networks-demystified-7-doing-co-citation-analyses/) by Scott Weingart to generate a co-citation graph from these articles.
4. I used Gephi to visualize the graph, filtering and resizing nodes by their centrality and displaying only those articles that strongly influenced other authors in the set.

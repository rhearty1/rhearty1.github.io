---
layout: post
title: Visualizing the community of engineering studies scholars
categories: [coding]
tags: [history, engineering]
---

I generated my second co-citation visualization
![](/assets/engineering-studies-co-citation.svg)  

What I did this time:
1.	Using Web of Science, I downloaded all 173 articles published in Engineering Studies from its inception until 30 November 2021.
2.	Created a co-citation network using Sci2tool and [this tutorial](http://scottbot.net/networks-demystified-7-doing-co-citation-analyses/).
3.	In Sci2tool, I removed any edge between articles unless they’ve been cited together more than once.
4.	In Sci2tool, I removed any remaining isolated components and the small islands, focusing instead on the “blob,” the single strongly connected component shown here.
5.	In Gephi, I clarified the visualization using [these suggestions](https://www.youtube.com/watch?v=f6ElMvP7ubs). For instance, I color-coated based on modularity class (clusters of articles that tended to cite each other more than the others).

There were a few modularity classes. The largest, in purple, was greatly influenced by the work of Wendy Faulkner.

![](/assets/engineering-studies-co-citation/purple.png)

Next largest were in blue, green, orange, and gray.

![](/assets/engineering-studies-co-citation/blue.png)

![](/assets/engineering-studies-co-citation/green.png)

![](/assets/engineering-studies-co-citation/orange.png)

![](/assets/engineering-studies-co-citation/gray.png)

Two smaller ones worth noting are in light gray and pink.

![](/assets/engineering-studies-co-citation/pink.png)

![](/assets/engineering-studies-co-citation/light-gray.png)

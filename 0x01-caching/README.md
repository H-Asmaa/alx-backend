# 0x01-caching
### Table of content
- [Introduction to caching](#introduction-to-caching)
- [What FIFO means](#what-fifo-means)
- [What LIFO means](#what-lifo-means)
- [What LRU means](#what-lru-means)
- [What MRU means](#what-mru-means)
- [What LFU means](#what-lfu-means)
- [What the purpose of a caching system](#what-the-purpose-of-a-caching-system)
- [What limits a caching system have](#what-limits-a-caching-system-have)

## Introduction to caching
You know when you wear a peice of clothing and you keep it in an easily accessible place so that you can get it fast. There might be different reasons for that, the peice of clothes might be one of your favorites, or it might be because you wear it more often...

same for caching, the caching is a technique in computing to store and manage data that can be reused. It allows faster access to frequently used information by storing it in memory.

This technique can be implemented in hardware as well as in software... There are different algorithms that can be used to acheive such thing, which are exactly what we are going to extend in in this file.

## What FIFO means
First in First Out. It is a Queue like structure. The data which comes first will be removed first.

## What LIFO means
Last in First Out. It is a Stack like structure. The last data most recently added is the first to be removed.

## What LRU means
Least Recently Used. The data least recently used will be removed. It is often done using timestamp or a counter.

## What MRU means
Most Recently Used. The data most recently used will be removed.

## What LFU means
Least Freaquently Used. The data least freaquently used will be removed first.

## What the purpose of a caching system
## What limits a caching system have

#!/usr/bin/env python
# coding: utf-8

# In[1]:


def data_grab():
    """importing data function"""
    import os
    import pandas as pd
    import pymysql
    import csv
    from sqlalchemy import create_engine, types


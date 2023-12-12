# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 14:34:43 2023

@author: shahr
"""

import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header ('st.write')


st.write ('Hello, world!')

df = pd.DataFrame({
    'first column': [1,2,3,4],
    'second column': [10,20,30,40]
    })

st.write(df)

st.write ('Below is dataframe:', df, 'Above is dataframe.')

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)

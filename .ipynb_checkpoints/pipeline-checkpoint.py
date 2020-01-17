{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import numpy as np\n",
    "import csv\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "os.chdir('C:/Users/aciag/WebDataPipeline/data')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "df=pd.read_csv('GSAF5.csv', encoding='latin_1')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(5992, 24)"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Case Number                  0\n",
       "Date                         0\n",
       "Year                         0\n",
       "Type                         0\n",
       "Country                     43\n",
       "Area                       402\n",
       "Location                   496\n",
       "Activity                   527\n",
       "Name                       200\n",
       "Sex                        567\n",
       "Age                       2681\n",
       "Injury                      27\n",
       "Fatal (Y/N)                 19\n",
       "Time                      3213\n",
       "Species                   2934\n",
       "Investigator or Source      15\n",
       "pdf                          0\n",
       "href formula                 1\n",
       "href                         3\n",
       "Case Number.1                0\n",
       "Case Number.2                0\n",
       "original order               0\n",
       "Unnamed: 22               5991\n",
       "Unnamed: 23               5990\n",
       "dtype: int64"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isna().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Case Number</th>\n",
       "      <th>Date</th>\n",
       "      <th>Year</th>\n",
       "      <th>Type</th>\n",
       "      <th>Country</th>\n",
       "      <th>Area</th>\n",
       "      <th>Location</th>\n",
       "      <th>Activity</th>\n",
       "      <th>Name</th>\n",
       "      <th>Sex</th>\n",
       "      <th>...</th>\n",
       "      <th>Species</th>\n",
       "      <th>Investigator or Source</th>\n",
       "      <th>pdf</th>\n",
       "      <th>href formula</th>\n",
       "      <th>href</th>\n",
       "      <th>Case Number.1</th>\n",
       "      <th>Case Number.2</th>\n",
       "      <th>original order</th>\n",
       "      <th>Unnamed: 22</th>\n",
       "      <th>Unnamed: 23</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>0</td>\n",
       "      <td>2016.09.18.c</td>\n",
       "      <td>18-Sep-16</td>\n",
       "      <td>2016</td>\n",
       "      <td>Unprovoked</td>\n",
       "      <td>USA</td>\n",
       "      <td>Florida</td>\n",
       "      <td>New Smyrna Beach, Volusia County</td>\n",
       "      <td>Surfing</td>\n",
       "      <td>male</td>\n",
       "      <td>M</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Orlando Sentinel, 9/19/2016</td>\n",
       "      <td>2016.09.18.c-NSB.pdf</td>\n",
       "      <td>http://sharkattackfile.net/spreadsheets/pdf_di...</td>\n",
       "      <td>http://sharkattackfile.net/spreadsheets/pdf_di...</td>\n",
       "      <td>2016.09.18.c</td>\n",
       "      <td>2016.09.18.c</td>\n",
       "      <td>5993</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1</td>\n",
       "      <td>2016.09.18.b</td>\n",
       "      <td>18-Sep-16</td>\n",
       "      <td>2016</td>\n",
       "      <td>Unprovoked</td>\n",
       "      <td>USA</td>\n",
       "      <td>Florida</td>\n",
       "      <td>New Smyrna Beach, Volusia County</td>\n",
       "      <td>Surfing</td>\n",
       "      <td>Chucky Luciano</td>\n",
       "      <td>M</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Orlando Sentinel, 9/19/2016</td>\n",
       "      <td>2016.09.18.b-Luciano.pdf</td>\n",
       "      <td>http://sharkattackfile.net/spreadsheets/pdf_di...</td>\n",
       "      <td>http://sharkattackfile.net/spreadsheets/pdf_di...</td>\n",
       "      <td>2016.09.18.b</td>\n",
       "      <td>2016.09.18.b</td>\n",
       "      <td>5992</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2</td>\n",
       "      <td>2016.09.18.a</td>\n",
       "      <td>18-Sep-16</td>\n",
       "      <td>2016</td>\n",
       "      <td>Unprovoked</td>\n",
       "      <td>USA</td>\n",
       "      <td>Florida</td>\n",
       "      <td>New Smyrna Beach, Volusia County</td>\n",
       "      <td>Surfing</td>\n",
       "      <td>male</td>\n",
       "      <td>M</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Orlando Sentinel, 9/19/2016</td>\n",
       "      <td>2016.09.18.a-NSB.pdf</td>\n",
       "      <td>http://sharkattackfile.net/spreadsheets/pdf_di...</td>\n",
       "      <td>http://sharkattackfile.net/spreadsheets/pdf_di...</td>\n",
       "      <td>2016.09.18.a</td>\n",
       "      <td>2016.09.18.a</td>\n",
       "      <td>5991</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>3</td>\n",
       "      <td>2016.09.17</td>\n",
       "      <td>17-Sep-16</td>\n",
       "      <td>2016</td>\n",
       "      <td>Unprovoked</td>\n",
       "      <td>AUSTRALIA</td>\n",
       "      <td>Victoria</td>\n",
       "      <td>Thirteenth Beach</td>\n",
       "      <td>Surfing</td>\n",
       "      <td>Rory Angiolella</td>\n",
       "      <td>M</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>The Age, 9/18/2016</td>\n",
       "      <td>2016.09.17-Angiolella.pdf</td>\n",
       "      <td>http://sharkattackfile.net/spreadsheets/pdf_di...</td>\n",
       "      <td>http://sharkattackfile.net/spreadsheets/pdf_di...</td>\n",
       "      <td>2016.09.17</td>\n",
       "      <td>2016.09.17</td>\n",
       "      <td>5990</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>4</td>\n",
       "      <td>2016.09.15</td>\n",
       "      <td>16-Sep-16</td>\n",
       "      <td>2016</td>\n",
       "      <td>Unprovoked</td>\n",
       "      <td>AUSTRALIA</td>\n",
       "      <td>Victoria</td>\n",
       "      <td>Bells Beach</td>\n",
       "      <td>Surfing</td>\n",
       "      <td>male</td>\n",
       "      <td>M</td>\n",
       "      <td>...</td>\n",
       "      <td>2 m shark</td>\n",
       "      <td>The Age, 9/16/2016</td>\n",
       "      <td>2016.09.16-BellsBeach.pdf</td>\n",
       "      <td>http://sharkattackfile.net/spreadsheets/pdf_di...</td>\n",
       "      <td>http://sharkattackfile.net/spreadsheets/pdf_di...</td>\n",
       "      <td>2016.09.16</td>\n",
       "      <td>2016.09.15</td>\n",
       "      <td>5989</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 24 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "    Case Number       Date  Year        Type    Country      Area  \\\n",
       "0  2016.09.18.c  18-Sep-16  2016  Unprovoked        USA   Florida   \n",
       "1  2016.09.18.b  18-Sep-16  2016  Unprovoked        USA   Florida   \n",
       "2  2016.09.18.a  18-Sep-16  2016  Unprovoked        USA   Florida   \n",
       "3    2016.09.17  17-Sep-16  2016  Unprovoked  AUSTRALIA  Victoria   \n",
       "4    2016.09.15  16-Sep-16  2016  Unprovoked  AUSTRALIA  Victoria   \n",
       "\n",
       "                           Location Activity             Name Sex   ...  \\\n",
       "0  New Smyrna Beach, Volusia County  Surfing             male    M  ...   \n",
       "1  New Smyrna Beach, Volusia County  Surfing   Chucky Luciano    M  ...   \n",
       "2  New Smyrna Beach, Volusia County  Surfing             male    M  ...   \n",
       "3                  Thirteenth Beach  Surfing  Rory Angiolella    M  ...   \n",
       "4                       Bells Beach  Surfing             male    M  ...   \n",
       "\n",
       "    Species        Investigator or Source                        pdf  \\\n",
       "0        NaN  Orlando Sentinel, 9/19/2016       2016.09.18.c-NSB.pdf   \n",
       "1        NaN  Orlando Sentinel, 9/19/2016   2016.09.18.b-Luciano.pdf   \n",
       "2        NaN  Orlando Sentinel, 9/19/2016       2016.09.18.a-NSB.pdf   \n",
       "3        NaN           The Age, 9/18/2016  2016.09.17-Angiolella.pdf   \n",
       "4  2 m shark           The Age, 9/16/2016  2016.09.16-BellsBeach.pdf   \n",
       "\n",
       "                                        href formula  \\\n",
       "0  http://sharkattackfile.net/spreadsheets/pdf_di...   \n",
       "1  http://sharkattackfile.net/spreadsheets/pdf_di...   \n",
       "2  http://sharkattackfile.net/spreadsheets/pdf_di...   \n",
       "3  http://sharkattackfile.net/spreadsheets/pdf_di...   \n",
       "4  http://sharkattackfile.net/spreadsheets/pdf_di...   \n",
       "\n",
       "                                                href Case Number.1  \\\n",
       "0  http://sharkattackfile.net/spreadsheets/pdf_di...  2016.09.18.c   \n",
       "1  http://sharkattackfile.net/spreadsheets/pdf_di...  2016.09.18.b   \n",
       "2  http://sharkattackfile.net/spreadsheets/pdf_di...  2016.09.18.a   \n",
       "3  http://sharkattackfile.net/spreadsheets/pdf_di...    2016.09.17   \n",
       "4  http://sharkattackfile.net/spreadsheets/pdf_di...    2016.09.16   \n",
       "\n",
       "  Case Number.2 original order Unnamed: 22 Unnamed: 23  \n",
       "0  2016.09.18.c           5993         NaN         NaN  \n",
       "1  2016.09.18.b           5992         NaN         NaN  \n",
       "2  2016.09.18.a           5991         NaN         NaN  \n",
       "3    2016.09.17           5990         NaN         NaN  \n",
       "4    2016.09.15           5989         NaN         NaN  \n",
       "\n",
       "[5 rows x 24 columns]"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['Minor injury to thigh', 'Lacerations to hands',\n",
       "       'Lacerations to lower leg', ..., 'FATAL, leg stripped of flesh  ',\n",
       "       'FATAL, knocked overboard by tail of shark & carried off by shark ',\n",
       "       'FATAL. \"Shark bit him in half, carrying away the lower extremities\" '],\n",
       "      dtype=object)"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#df.drop(['Case Number', 'Name', 'Sex ', 'Species ', 'pdf', 'href formula', 'href'], axis=1, inplace=True)\n",
    "#df.drop(['Case Number.1', 'Case Number.2', 'original order', 'Unnamed: 22', 'Unnamed: 23'], axis=1, inplace=True)\n",
    "#df.drop(['Time', 'Investigator or Source', 'Age'], axis=1, inplace=True)\n",
    "\n",
    "df.Injury.unique()\n",
    "\n",
    "df.loc[df.trany.str.lower().str.contains('fatal').fillna(False), 'typeofinjury']='fatal'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Case Number', 'Date', 'Year', 'Type', 'Country', 'Area', 'Location', 'Activity', 'Name', 'Sex', 'Age', 'Injury', 'Fatal (Y/N)', 'Time', 'Species', 'Investigator or Source', 'pdf', 'href formula', 'href', 'Case Number.1', 'Case Number.2', 'original order', 'Unnamed: 22', 'Unnamed: 23']\n"
     ]
    }
   ],
   "source": [
    "cols=[]\n",
    "#remove spaces at the start and end of column names\n",
    "for i in df.columns:\n",
    "    if i.endswith(' ') or i.startswith(' '):\n",
    "        cols.append(i.rstrip())\n",
    "    else:\n",
    "        cols.append(i)\n",
    "        \n",
    "print(cols)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Case Number', 'Date', 'Year', 'Type', 'Country', 'Area', 'Location',\n",
       "       'Activity', 'Name', 'Sex', 'Age', 'Injury', 'Fatal (Y/N)', 'Time',\n",
       "       'Species', 'Investigator or Source', 'pdf', 'href formula', 'href',\n",
       "       'Case Number.1', 'Case Number.2', 'original order', 'Unnamed: 22',\n",
       "       'Unnamed: 23'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.columns=cols"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Given the objective of our research, some of the existing columns in database are either completely irrelevant or don't have any valuable data. Also dropping columns with PII and duplicates.\n",
    "\n",
    "Thus, we drop columns named:\n",
    "'Name', 'Sex', 'Age', 'Time', 'Species', 'Investigator or Source', 'pdf', 'href formula', 'href', 'Case Number.1', 'Case Number.2', 'original order', 'Unnamed: 22', 'Unnamed: 23'\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Name', 'Sex', 'Age', 'Time', 'Species', 'Investigator or Source', 'pdf', 'href formula', 'href', 'Case Number.1', 'Case Number.2', 'original order', 'Unnamed: 22', 'Unnamed: 23']\n"
     ]
    }
   ],
   "source": [
    "drop_cols=['Name', 'Sex', 'Age', 'Time', 'Species', 'Investigator or Source', 'pdf', 'href formula', 'href', 'Case Number.1', 'Case Number.2', 'original order', 'Unnamed: 22', 'Unnamed: 23']\n",
    "print(drop_cols)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "ename": "KeyError",
     "evalue": "\"['Name' 'Sex' 'Age' 'Time' 'Species' 'Investigator or Source' 'pdf'\\n 'href formula' 'href' 'Case Number.1' 'Case Number.2' 'original order'\\n 'Unnamed: 22' 'Unnamed: 23'] not found in axis\"",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-45-270df36c53f3>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mdf\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mdf\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdrop\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdrop_cols\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0maxis\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m~\\Anaconda3\\lib\\site-packages\\pandas\\core\\frame.py\u001b[0m in \u001b[0;36mdrop\u001b[1;34m(self, labels, axis, index, columns, level, inplace, errors)\u001b[0m\n\u001b[0;32m   4100\u001b[0m             \u001b[0mlevel\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mlevel\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   4101\u001b[0m             \u001b[0minplace\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0minplace\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 4102\u001b[1;33m             \u001b[0merrors\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0merrors\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   4103\u001b[0m         )\n\u001b[0;32m   4104\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\site-packages\\pandas\\core\\generic.py\u001b[0m in \u001b[0;36mdrop\u001b[1;34m(self, labels, axis, index, columns, level, inplace, errors)\u001b[0m\n\u001b[0;32m   3912\u001b[0m         \u001b[1;32mfor\u001b[0m \u001b[0maxis\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mlabels\u001b[0m \u001b[1;32min\u001b[0m \u001b[0maxes\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mitems\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   3913\u001b[0m             \u001b[1;32mif\u001b[0m \u001b[0mlabels\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 3914\u001b[1;33m                 \u001b[0mobj\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mobj\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_drop_axis\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mlabels\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0maxis\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mlevel\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mlevel\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0merrors\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0merrors\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   3915\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   3916\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0minplace\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\site-packages\\pandas\\core\\generic.py\u001b[0m in \u001b[0;36m_drop_axis\u001b[1;34m(self, labels, axis, level, errors)\u001b[0m\n\u001b[0;32m   3944\u001b[0m                 \u001b[0mnew_axis\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0maxis\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdrop\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mlabels\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mlevel\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mlevel\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0merrors\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0merrors\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   3945\u001b[0m             \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 3946\u001b[1;33m                 \u001b[0mnew_axis\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0maxis\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdrop\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mlabels\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0merrors\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0merrors\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   3947\u001b[0m             \u001b[0mresult\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mreindex\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m**\u001b[0m\u001b[1;33m{\u001b[0m\u001b[0maxis_name\u001b[0m\u001b[1;33m:\u001b[0m \u001b[0mnew_axis\u001b[0m\u001b[1;33m}\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   3948\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\site-packages\\pandas\\core\\indexes\\base.py\u001b[0m in \u001b[0;36mdrop\u001b[1;34m(self, labels, errors)\u001b[0m\n\u001b[0;32m   5338\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mmask\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0many\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   5339\u001b[0m             \u001b[1;32mif\u001b[0m \u001b[0merrors\u001b[0m \u001b[1;33m!=\u001b[0m \u001b[1;34m\"ignore\"\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 5340\u001b[1;33m                 \u001b[1;32mraise\u001b[0m \u001b[0mKeyError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"{} not found in axis\"\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mformat\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mlabels\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mmask\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   5341\u001b[0m             \u001b[0mindexer\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mindexer\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;33m~\u001b[0m\u001b[0mmask\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   5342\u001b[0m         \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdelete\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mindexer\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mKeyError\u001b[0m: \"['Name' 'Sex' 'Age' 'Time' 'Species' 'Investigator or Source' 'pdf'\\n 'href formula' 'href' 'Case Number.1' 'Case Number.2' 'original order'\\n 'Unnamed: 22' 'Unnamed: 23'] not found in axis\""
     ]
    }
   ],
   "source": [
    "df=df.drop(drop_cols, axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Case Number</th>\n",
       "      <th>Date</th>\n",
       "      <th>Year</th>\n",
       "      <th>Type</th>\n",
       "      <th>Country</th>\n",
       "      <th>Area</th>\n",
       "      <th>Location</th>\n",
       "      <th>Activity</th>\n",
       "      <th>Injury</th>\n",
       "      <th>Fatal (Y/N)</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>0</td>\n",
       "      <td>2016.09.18.c</td>\n",
       "      <td>18-Sep-16</td>\n",
       "      <td>2016</td>\n",
       "      <td>Unprovoked</td>\n",
       "      <td>USA</td>\n",
       "      <td>Florida</td>\n",
       "      <td>New Smyrna Beach, Volusia County</td>\n",
       "      <td>Surfing</td>\n",
       "      <td>Minor injury to thigh</td>\n",
       "      <td>N</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1</td>\n",
       "      <td>2016.09.18.b</td>\n",
       "      <td>18-Sep-16</td>\n",
       "      <td>2016</td>\n",
       "      <td>Unprovoked</td>\n",
       "      <td>USA</td>\n",
       "      <td>Florida</td>\n",
       "      <td>New Smyrna Beach, Volusia County</td>\n",
       "      <td>Surfing</td>\n",
       "      <td>Lacerations to hands</td>\n",
       "      <td>N</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2</td>\n",
       "      <td>2016.09.18.a</td>\n",
       "      <td>18-Sep-16</td>\n",
       "      <td>2016</td>\n",
       "      <td>Unprovoked</td>\n",
       "      <td>USA</td>\n",
       "      <td>Florida</td>\n",
       "      <td>New Smyrna Beach, Volusia County</td>\n",
       "      <td>Surfing</td>\n",
       "      <td>Lacerations to lower leg</td>\n",
       "      <td>N</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>3</td>\n",
       "      <td>2016.09.17</td>\n",
       "      <td>17-Sep-16</td>\n",
       "      <td>2016</td>\n",
       "      <td>Unprovoked</td>\n",
       "      <td>AUSTRALIA</td>\n",
       "      <td>Victoria</td>\n",
       "      <td>Thirteenth Beach</td>\n",
       "      <td>Surfing</td>\n",
       "      <td>Struck by fin on chest &amp; leg</td>\n",
       "      <td>N</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>4</td>\n",
       "      <td>2016.09.15</td>\n",
       "      <td>16-Sep-16</td>\n",
       "      <td>2016</td>\n",
       "      <td>Unprovoked</td>\n",
       "      <td>AUSTRALIA</td>\n",
       "      <td>Victoria</td>\n",
       "      <td>Bells Beach</td>\n",
       "      <td>Surfing</td>\n",
       "      <td>No injury: Knocked off board by shark</td>\n",
       "      <td>N</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    Case Number       Date  Year        Type    Country      Area  \\\n",
       "0  2016.09.18.c  18-Sep-16  2016  Unprovoked        USA   Florida   \n",
       "1  2016.09.18.b  18-Sep-16  2016  Unprovoked        USA   Florida   \n",
       "2  2016.09.18.a  18-Sep-16  2016  Unprovoked        USA   Florida   \n",
       "3    2016.09.17  17-Sep-16  2016  Unprovoked  AUSTRALIA  Victoria   \n",
       "4    2016.09.15  16-Sep-16  2016  Unprovoked  AUSTRALIA  Victoria   \n",
       "\n",
       "                           Location Activity  \\\n",
       "0  New Smyrna Beach, Volusia County  Surfing   \n",
       "1  New Smyrna Beach, Volusia County  Surfing   \n",
       "2  New Smyrna Beach, Volusia County  Surfing   \n",
       "3                  Thirteenth Beach  Surfing   \n",
       "4                       Bells Beach  Surfing   \n",
       "\n",
       "                                  Injury Fatal (Y/N)  \n",
       "0                  Minor injury to thigh           N  \n",
       "1                   Lacerations to hands           N  \n",
       "2               Lacerations to lower leg           N  \n",
       "3           Struck by fin on chest & leg           N  \n",
       "4  No injury: Knocked off board by shark           N  "
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['USA', 'AUSTRALIA', 'NEW CALEDONIA', 'REUNION', 'BAHAMAS', 'SPAIN',\n",
       "       'CHINA', 'JAPAN', 'COLUMBIA', 'SOUTH AFRICA', 'EGYPT',\n",
       "       'NEW ZEALAND', 'INDONESIA', 'FRENCH POLYNESIA', 'CAPE VERDE',\n",
       "       'Fiji', 'BRAZIL', 'DOMINICAN REPUBLIC', 'CAYMAN ISLANDS',\n",
       "       'UNITED ARAB EMIRATES', 'ARUBA', 'MOZAMBIQUE', 'THAILAND', 'FIJI',\n",
       "       'PUERTO RICO', 'ITALY', 'MEXICO', 'ATLANTIC OCEAN', 'GREECE',\n",
       "       'MAURITIUS', nan, 'ST. MARTIN', 'FRANCE', 'ECUADOR',\n",
       "       'PAPUA NEW GUINEA', 'TRINIDAD & TOBAGO', 'KIRIBATI', 'ISRAEL',\n",
       "       'DIEGO GARCIA', 'TAIWAN', 'JAMAICA', 'PALESTINIAN TERRITORIES',\n",
       "       'GUAM', 'SEYCHELLES', 'BELIZE', 'PHILIPPINES', 'NIGERIA', 'TONGA',\n",
       "       'SCOTLAND', 'CANADA', 'CROATIA', 'SAUDI ARABIA', 'CHILE',\n",
       "       'ANTIGUA', 'KENYA', 'RUSSIA', 'TURKS & CAICOS', 'COSTA RICA',\n",
       "       'UNITED KINGDOM', 'MALAYSIA', 'UNITED ARAB EMIRATES (UAE)',\n",
       "       'SAMOA', 'AZORES', 'SOLOMON ISLANDS', 'SOUTH KOREA', 'MALTA',\n",
       "       'VIETNAM', 'MADAGASCAR', 'PANAMA', 'SOMALIA', 'NEVIS', 'CUBA',\n",
       "       'ENGLAND', 'BRITISH VIRGIN ISLANDS', 'NORWAY', 'SENEGAL', 'YEMEN',\n",
       "       'GULF OF ADEN', 'Sierra Leone', 'ST. MAARTIN', 'GRAND CAYMAN',\n",
       "       'Seychelles', 'LIBERIA', 'VANUATU', 'MEXICO ', 'HONDURAS',\n",
       "       'VENEZUELA', 'SRI LANKA', ' TONGA', 'URUGUAY', 'INDIA',\n",
       "       'MICRONESIA', 'CARIBBEAN SEA', 'OKINAWA', 'TANZANIA',\n",
       "       'MARSHALL ISLANDS', 'EGYPT / ISRAEL', 'NORTHERN ARABIAN SEA',\n",
       "       'HONG KONG', 'EL SALVADOR', 'ANGOLA', 'BERMUDA', 'MONTENEGRO',\n",
       "       'IRAN', 'TUNISIA', 'NAMIBIA', 'NORTH ATLANTIC OCEAN', 'PORTUGAL',\n",
       "       'SOUTH CHINA SEA', 'BANGLADESH', 'PALAU', 'WESTERN SAMOA',\n",
       "       'PACIFIC OCEAN ', 'BRITISH ISLES', 'GRENADA', 'IRAQ', 'TURKEY',\n",
       "       'SINGAPORE', 'NEW BRITAIN', 'SUDAN', 'JOHNSTON ISLAND',\n",
       "       'SOUTH PACIFIC OCEAN', 'NEW GUINEA', 'RED SEA',\n",
       "       'NORTH PACIFIC OCEAN', 'FEDERATED STATES OF MICRONESIA',\n",
       "       'MID ATLANTIC OCEAN', 'ADMIRALTY ISLANDS', 'BRITISH WEST INDIES',\n",
       "       'SOUTH ATLANTIC OCEAN', 'PERSIAN GULF', 'RED SEA / INDIAN OCEAN',\n",
       "       'PACIFIC OCEAN', 'NORTH SEA', 'NICARAGUA ', 'MALDIVE ISLANDS',\n",
       "       'AMERICAN SAMOA', 'ANDAMAN / NICOBAR ISLANDAS', 'GABON', 'MAYOTTE',\n",
       "       'NORTH ATLANTIC OCEAN ', 'THE BALKANS', 'SUDAN?', 'ARGENTINA',\n",
       "       'MARTINIQUE', 'INDIAN OCEAN', 'GUATEMALA', 'NETHERLANDS ANTILLES',\n",
       "       'NORTHERN MARIANA ISLANDS', 'IRAN / IRAQ', 'JAVA', 'SIERRA LEONE',\n",
       "       ' PHILIPPINES', 'NICARAGUA', 'CENTRAL PACIFIC',\n",
       "       'SOLOMON ISLANDS / VANUATU', 'SOUTHWEST PACIFIC OCEAN',\n",
       "       'BAY OF BENGAL', 'MID-PACIFC OCEAN', 'SLOVENIA', 'CURACAO',\n",
       "       'ITALY / CROATIA', 'BARBADOS', 'MONACO', 'GUYANA', 'HAITI',\n",
       "       'SAN DOMINGO', 'IRELAND', 'KUWAIT', 'LIBYA', 'YEMEN ',\n",
       "       'MEDITERRANEAN SEA?', 'FALKLAND ISLANDS', 'CRETE', 'CYPRUS',\n",
       "       'EGYPT ', 'BURMA', 'LEBANON', 'PARAGUAY', 'BRITISH NEW GUINEA',\n",
       "       'OCEAN', 'GEORGIA', 'SYRIA', 'TUVALU', 'INDIAN OCEAN?', 'GUINEA',\n",
       "       'EQUATORIAL GUINEA / CAMEROON', 'COOK ISLANDS', 'ALGERIA',\n",
       "       'Coast of AFRICA', 'TASMAN SEA', 'GHANA', 'St Helena', 'GREENLAND',\n",
       "       'MEDITERRANEAN SEA', 'SWEDEN', 'ICELAND',\n",
       "       'Between PORTUGAL & INDIA', 'DJIBOUTI', 'BAHREIN', 'KOREA',\n",
       "       'RED SEA?', 'ASIA?', 'CEYLON (SRI LANKA)'], dtype=object)"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.Country.unique()\n",
    "\n",
    "#clean spaces "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import numpy as np"
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
    "import pymysql\n",
    "import csv\n",
    "import pandas as pd\n",
    "from sqlalchemy import create_engine, types\n",
    "\n",
    "username='root'\n",
    "host='localhost'\n",
    "database_name='sharks'\n",
    "password='Bat-chat25t'\n",
    "\n",
    "engine = create_engine(f\"mysql+pymysql://{username}:{password}@localhost/sharks\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "df=pd.read_csv('GSAF5.csv', encoding='latin_1')"
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
       "(5992, 24)"
      ]
     },
     "execution_count": 5,
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
   "execution_count": 6,
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
     "execution_count": 6,
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
   "execution_count": 7,
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
     "execution_count": 7,
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
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "df.drop(['Case Number', 'Name', 'Sex ', 'Species ', 'pdf', 'href formula', 'href'], axis=1, inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "df.drop(['Case Number.1', 'Case Number.2', 'original order', 'Unnamed: 22', 'Unnamed: 23'], axis=1, inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "df.drop(['Time', 'Investigator or Source', 'Age'], axis=1, inplace=True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
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
       "    <tr>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>5987</td>\n",
       "      <td>Before 1903</td>\n",
       "      <td>0</td>\n",
       "      <td>Unprovoked</td>\n",
       "      <td>AUSTRALIA</td>\n",
       "      <td>Western Australia</td>\n",
       "      <td>Roebuck Bay</td>\n",
       "      <td>Diving</td>\n",
       "      <td>FATAL</td>\n",
       "      <td>Y</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>5988</td>\n",
       "      <td>Before 1903</td>\n",
       "      <td>0</td>\n",
       "      <td>Unprovoked</td>\n",
       "      <td>AUSTRALIA</td>\n",
       "      <td>Western Australia</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Pearl diving</td>\n",
       "      <td>FATAL</td>\n",
       "      <td>Y</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>5989</td>\n",
       "      <td>1900-1905</td>\n",
       "      <td>0</td>\n",
       "      <td>Unprovoked</td>\n",
       "      <td>USA</td>\n",
       "      <td>North Carolina</td>\n",
       "      <td>Ocracoke Inlet</td>\n",
       "      <td>Swimming</td>\n",
       "      <td>FATAL</td>\n",
       "      <td>Y</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>5990</td>\n",
       "      <td>1883-1889</td>\n",
       "      <td>0</td>\n",
       "      <td>Unprovoked</td>\n",
       "      <td>PANAMA</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Panama Bay 8ºN, 79ºW</td>\n",
       "      <td>NaN</td>\n",
       "      <td>FATAL</td>\n",
       "      <td>Y</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>5991</td>\n",
       "      <td>1845-1853</td>\n",
       "      <td>0</td>\n",
       "      <td>Unprovoked</td>\n",
       "      <td>CEYLON (SRI LANKA)</td>\n",
       "      <td>Eastern Province</td>\n",
       "      <td>Below the English fort, Trincomalee</td>\n",
       "      <td>Swimming</td>\n",
       "      <td>FATAL. \"Shark bit him in half, carrying away t...</td>\n",
       "      <td>Y</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5992 rows × 9 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "             Date  Year        Type             Country               Area  \\\n",
       "0       18-Sep-16  2016  Unprovoked                 USA            Florida   \n",
       "1       18-Sep-16  2016  Unprovoked                 USA            Florida   \n",
       "2       18-Sep-16  2016  Unprovoked                 USA            Florida   \n",
       "3       17-Sep-16  2016  Unprovoked           AUSTRALIA           Victoria   \n",
       "4       16-Sep-16  2016  Unprovoked           AUSTRALIA           Victoria   \n",
       "...           ...   ...         ...                 ...                ...   \n",
       "5987  Before 1903     0  Unprovoked           AUSTRALIA  Western Australia   \n",
       "5988  Before 1903     0  Unprovoked           AUSTRALIA  Western Australia   \n",
       "5989    1900-1905     0  Unprovoked                 USA     North Carolina   \n",
       "5990    1883-1889     0  Unprovoked              PANAMA                NaN   \n",
       "5991    1845-1853     0  Unprovoked  CEYLON (SRI LANKA)   Eastern Province   \n",
       "\n",
       "                                 Location      Activity  \\\n",
       "0        New Smyrna Beach, Volusia County       Surfing   \n",
       "1        New Smyrna Beach, Volusia County       Surfing   \n",
       "2        New Smyrna Beach, Volusia County       Surfing   \n",
       "3                        Thirteenth Beach       Surfing   \n",
       "4                             Bells Beach       Surfing   \n",
       "...                                   ...           ...   \n",
       "5987                          Roebuck Bay        Diving   \n",
       "5988                                  NaN  Pearl diving   \n",
       "5989                       Ocracoke Inlet      Swimming   \n",
       "5990                 Panama Bay 8ºN, 79ºW           NaN   \n",
       "5991  Below the English fort, Trincomalee      Swimming   \n",
       "\n",
       "                                                 Injury Fatal (Y/N)  \n",
       "0                                 Minor injury to thigh           N  \n",
       "1                                  Lacerations to hands           N  \n",
       "2                              Lacerations to lower leg           N  \n",
       "3                          Struck by fin on chest & leg           N  \n",
       "4                 No injury: Knocked off board by shark           N  \n",
       "...                                                 ...         ...  \n",
       "5987                                              FATAL           Y  \n",
       "5988                                              FATAL           Y  \n",
       "5989                                              FATAL           Y  \n",
       "5990                                              FATAL           Y  \n",
       "5991  FATAL. \"Shark bit him in half, carrying away t...           Y  \n",
       "\n",
       "[5992 rows x 9 columns]"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
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
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.Injury.unique()"
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

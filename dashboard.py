import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.write(
    """
    # My first app
    Hello, para calon praktisi data masa depan!
    """
)
# Judul aplikasi
st.title('Visualisasi Data Sewa Sepeda')

# Upload file CSV
file = st.file_uploader('Upload file CSV', type=['csv'])

# Jika file sudah diunggah
if file is not None:
    # Membaca file CSV
    data = pd.read_csv(file)
    
    # Menampilkan histogram dari data
    st.write('## Histogram Data')
    st.write(data.hist())
    
    # Menghitung jumlah sewa sepeda per jam
    hourly_demand = data.groupby('hr')['cnt'].mean().reset_index()

    # Menghitung jumlah sewa sepeda per hari dalam seminggu
    daily_demand = data.groupby('weekday')['cnt'].mean().reset_index()

    # Menghitung jumlah sewa sepeda per bulan
    monthly_demand = data.groupby('mnth')['cnt'].mean().reset_index()

    # Menghitung jumlah sewa sepeda per musim
    seasonal_demand = data.groupby('season')['cnt'].mean().reset_index()

    # Visualisasi pola harian
    st.write('## Pola Permintaan Sewa Sepeda Harian')
    plt.figure(figsize=(10, 6))
    plt.plot(hourly_demand['hr'], hourly_demand['cnt'])
    plt.title('Pola Permintaan Sewa Sepeda Harian')
    plt.xlabel('Jam')
    plt.ylabel('Jumlah Sewa Sepeda')
    st.pyplot()

    # Visualisasi pola mingguan
    st.write('## Pola Permintaan Sewa Sepeda Mingguan')
    plt.figure(figsize=(10, 6))
    plt.bar(daily_demand['weekday'], daily_demand['cnt'])
    plt.title('Pola Permintaan Sewa Sepeda Mingguan')
    plt.xlabel('Hari dalam Seminggu')
    plt.ylabel('Jumlah Sewa Sepeda')
    st.pyplot()

    # Visualisasi pola bulanan
    st.write('## Pola Permintaan Sewa Sepeda Bulanan')
    plt.figure(figsize=(10, 6))
    plt.bar(monthly_demand['mnth'], monthly_demand['cnt'])
    plt.title('Pola Permintaan Sewa Sepeda Bulanan')
    plt.xlabel('Bulan')
    plt.ylabel('Jumlah Sewa Sepeda')
    st.pyplot()

    # Visualisasi pola musiman
    st.write('## Pola Permintaan Sewa Sepeda Musiman')
    plt.figure(figsize=(10, 6))
    plt.bar(seasonal_demand['season'], seasonal_demand['cnt'])
    plt.title('Pola Permintaan Sewa Sepeda Musiman')
    plt.xlabel('Musim')
    plt.ylabel('Jumlah Sewa Sepeda')
    st.pyplot()

    # Menghitung korelasi antara fitur dan jumlah sewa sepeda
    corr = data.corr()['cnt'].drop('cnt')
    st.write("## Korelasi antara fitur dan jumlah sewa sepeda:")
    st.write(corr)

    # Visualisasi pengaruh cuaca terhadap jumlah sewa sepeda
    st.write('## Pengaruh Cuaca terhadap Jumlah Sewa Sepeda')
    plt.figure(figsize=(10, 6))
    sns.barplot(x='weathersit', y='cnt', data=data)
    plt.title('Pengaruh Cuaca terhadap Jumlah Sewa Sepeda')
    plt.xlabel('Kondisi Cuaca')
    plt.ylabel('Jumlah Sewa Sepeda')
    st.pyplot()

    # Visualisasi pengaruh hari libur terhadap jumlah sewa sepeda
    st.write('## Pengaruh Hari Libur terhadap Jumlah Sewa Sepeda')
    plt.figure(figsize=(10, 6))
    sns.barplot(x='holiday', y='cnt', data=data)
    plt.title('Pengaruh Hari Libur terhadap Jumlah Sewa Sepeda')
    plt.xlabel('Hari Libur')
    plt.ylabel('Jumlah Sewa Sepeda')
    st.pyplot()

    # Visualisasi pengaruh akhir pekan terhadap jumlah sewa sepeda
    st.write('## Pengaruh Akhir Pekan terhadap Jumlah Sewa Sepeda')
    plt.figure(figsize=(10, 6))
    sns.barplot(x='workingday', y='cnt', data=data)
    plt.title('Pengaruh Akhir Pekan terhadap Jumlah Sewa Sepeda')
    plt.xlabel('Hari Kerja')
    plt

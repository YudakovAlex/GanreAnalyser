from scipy.io import wavfile
import matplotlib.pyplot as plt
import pandas as pd

folder = "/home/shad/Projects/GanreAnalizer/Samples/wav/"
files = [
        "Master_Exploder.wav",
        "Dragonbourn.wav",
        "No_Educcation.wav",
        "TNT.wav",
        "Too_Much_To-_Young.wav",
        "Your_Time_Has_Come.wav"
        ]

for f in files:
    print(f)
    fs, data = wavfile.read(folder + f)
    df_data = pd.DataFrame(data)
    df_data['max'] = df_data.max(axis=1)
    #print(df_data.describe())
    buckets = pd.cut(df_data['max'],10)
    tone_repetitions = df_data.groupby('max').size()
    df_data['1k group'] = pd.Series(df_data['max']/1000).astype(int)
    size_of_1k = df_data.groupby('1k group').size()
    
    plt.plot(size_of_1k)
    plt.show()
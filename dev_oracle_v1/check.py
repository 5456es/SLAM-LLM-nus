with open("/nfs/yangguanrou.ygr/slidespeech/test_oracle_v1/text",'r') as f:
    for line in f:
        if len(line.split())==1:
            print("fuck")
            print(line)

# YTB+b_aCA1P9Re8+00033 这句话的text是空的 在四个文件里删去了
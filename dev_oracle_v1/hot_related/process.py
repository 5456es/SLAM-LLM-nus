with open("/nfs/yangguanrou.ygr/slidespeech/dev_oracle_v1/hot_related/ocr_1gram_top50_mmr070_hotwords_list","r") as f:
    with open("/nfs/yangguanrou.ygr/slidespeech/dev_oracle_v1/hot_related/ocr_1gram_top50_mmr070_hotwords_list_lower","w") as f1:
        for line in f:
            line = line.strip().split(' ',1)
            
            if len(line) == 1:
                f1.write(line[0]+' '+'\n')
            else:
                line1 = line[1]
                line1 = line1.split('$')
                line1 = " ".join(line1)
                line1 = line1.lower()
                f1.write(line[0]+' '+line1+'\n')
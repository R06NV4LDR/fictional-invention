# Subsampling-Rechnung (vereinfachte Speicherreduktion)
# Verhältnis-Tabelle:
# 4:4:4 = 1.0, 4:2:2 = 0.67, 4:2:0 = 0.5

def subsampling_ratio(original_size_mb, mode):
    factor = {'4:4:4': 1.0, '4:2:2': 0.67, '4:2:0': 0.5}
    return round(original_size_mb * factor[mode], 2)

# Beispiel
print(subsampling_ratio(6, '4:2:0'))  # ergibt 3.0 MB
def levenshtein_distance(s1, s2):
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]

def similarity_percentage(s1, s2):
    len_s1 = len(s1)
    len_s2 = len(s2)
    distance = levenshtein_distance(s1, s2)
    max_len = max(len_s1, len_s2)
    similarity = 1 - (distance / max_len)
    return similarity * 100


# COmparacion de nombres ( una variable en comun)


# % de similitud a filtrar
similarity_threshold = 55

filtered_rows = []

for index, row in df.iterrows():
    sim_percentage = similarity_percentage(row["txt_nombre"], row["name"])
    if sim_percentage >= similarity_threshold:
        row["similitud_porcentaje"] = sim_percentage  # Agregar nueva columna
        filtered_rows.append(row)

filtered_df = pd.DataFrame(filtered_rows)

# comparacion de nombres y direcion en conjunto ( dos variables en comun)

# % de similitud a filtrar
similarity_name_threshold = 55
similarity_address_threshold = 40

filtered_rows = []

for index, row in df.iterrows():
    sim_name = similarity_percentage(row["txt_nombre"], row["name"])
    sim_address = similarity_percentage(row["txt_direccion"], row["name_of_street"])
    if sim_name >= similarity_name_threshold and sim_address >= similarity_address_threshold:
        row["similitud_nombre"] = sim_name
        row["similitud_direccion"] = sim_address
        filtered_rows.append(row)

filtered_df = pd.DataFrame(filtered_rows)



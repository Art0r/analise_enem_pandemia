for i in YEARS:
    with open(os.path.join(OUTPUT, f'describe{i}.txt'), 'w') as file:
        describe_provas = globals()[f'df_{i}'][PROVAS].describe(
            percentiles=[.15, .30, .45, .60, .75, .90],
            include=['object', 'float64', 'int64']
        ).apply(lambda s: np.round(s, 2))
        output = f"""
    ------------------------------------------------------------------------
    DESCRIÇÃO DA AMOSTRA

    {describe_provas}
    ------------------------------------------------------------------------
    """
        file.write(output)
        for j in 'ABCDE':
            describe_provas_classe = globals()[f'df_{i}'].query(f"Q006 == '{j}'")[PROVAS].describe(
                percentiles=[.15, .25, .30, .45, .60, .75, .90],
                include=['object', 'float64', 'int64']
            ).apply(lambda s: np.round(s, 2))

            output = f"""
    ------------------------------------------------------------------------
    DESCRIÇÃO DA AMOSTRA SOBRE A CLASSE {j}

    {describe_provas_classe}
    ------------------------------------------------------------------------
    """
            file.write(output)
        file.close()

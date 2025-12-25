def buildTable(data):

    table = []
   
    teams = data.keys()
    
    table.append("Tm,"+",".join(teams))
    
    rows = []
    for team in teams:
        row = team
        for otherTeam in teams:
            if team == otherTeam:
                row += ',--'
            else:
                row +=  ',' + str(data[team][otherTeam]['W']) 
        rows.append(row)
    table.extend(rows)
    return "\n".join(table)

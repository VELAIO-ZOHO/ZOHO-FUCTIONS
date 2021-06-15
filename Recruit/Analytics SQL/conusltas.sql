/* CONSULTAR OFERTAS ASOCIADAS A UN ANALISTA */
SELECT  "Título de la publicación", "Documento analista de selección responsable" FROM "Ofertas" WHERE "Documento analista de selección responsable" = 67011865


/* CONSULTAR OFERTAS ASOCIADAS A UN ANALISTA JOIN INFO ANALISTA */
SELECT  "Título de la publicación",  "ID de la requisición" FROM "Ofertas" WHERE "Seleccionadores asignados Id" = 594922000003107144 JOIN "Users" ON "Ofertas"."Seleccionadores asignados Id" = "Users"."USER_ID"
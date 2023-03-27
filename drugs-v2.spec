swagger: '2.0'
info:
  title: ''
  version: ''
host: api.cortellis.com
basePath: /api-ws/ws/rs/drugs-v2
schemes:
  - https
paths:
  '/company/taxonomy/{type}/{treecode}':
    parameters:
      - in: path
        name: type
        required: true
        type: string
      - in: path
        name: treecode
        required: true
        type: string
    get:
      responses:
        '200':
          description: Successful Response
  '/drug/SWOTs/{id}':
    parameters:
      - in: path
        name: id
        required: true
        type: string
    get:
      responses:
        '200':
          description: Successful Response
  '/drug/changeHistory/{id}':
    parameters:
      - in: path
        name: id
        required: true
        type: string
    get:
      responses:
        '200':
          description: Successful Response
  /drug/export/search/structure/:
    parameters: []
    get:
      parameters:
        - in: query
          name: query
          required: false
          type: string
        - in: query
          name: offset
          required: false
          type: string
        - in: query
          name: hits
          required: false
          type: string
        - in: query
          name: sortby
          required: false
          type: string
        - in: query
          name: sortBy
          required: false
          type: string
        - in: query
          name: fmt
          required: false
          type: string
      responses:
        '200':
          description: Successful Response
  /drug/export/search/structure/poll/:
    parameters: []
    get:
      parameters:
        - in: query
          name: token
          required: false
          type: string
      responses:
        '200':
          description: Successful Response
  /drug/export/structure/:
    parameters: []
    get:
      parameters:
        - in: query
          name: query
          required: false
          type: string
        - in: query
          name: offset
          required: false
          type: string
        - in: query
          name: hits
          required: false
          type: string
        - in: query
          name: sortby
          required: false
          type: string
        - in: query
          name: sortBy
          required: false
          type: string
        - in: query
          name: fmt
          required: false
          type: string
      responses:
        '200':
          description: Successful Response
  /drug/export/structure/poll/:
    parameters: []
    get:
      parameters:
        - in: query
          name: token
          required: false
          type: string
      responses:
        '200':
          description: Successful Response
  /drug/search:
    parameters: []
    get:
      parameters:
        - in: query
          name: query
          required: false
          type: string
        - in: query
          name: offset
          required: false
          type: string
        - in: query
          name: hits
          required: false
          type: string
        - in: query
          name: sortBy
          required: false
          type: string
        - in: query
          name: fmt
          required: false
          type: string
      responses:
        '200':
          description: Successful Response
  /drug/search/:
    parameters: []
    get:
      parameters:
        - in: query
          name: query
          required: false
          type: string
        - in: query
          name: offset
          required: false
          type: string
        - in: query
          name: hits
          required: false
          type: string
        - in: query
          name: sortby
          required: false
          type: string
        - in: query
          name: sortBy
          required: false
          type: string
        - in: query
          name: filtersEnabled
          required: false
          type: string
        - in: query
          name: querylanguage
          required: false
          type: string
        - in: query
          name: returnFilterCount
          required: false
          type: string
      responses:
        '200':
          description: Successful Response
  /drug/search/structure/:
    parameters: []
    get:
      parameters:
        - in: query
          name: query
          required: false
          type: string
        - in: query
          name: offset
          required: false
          type: string
        - in: query
          name: hits
          required: false
          type: string
        - in: query
          name: sortby
          required: false
          type: string
        - in: query
          name: sortBy
          required: false
          type: string
        - in: query
          name: filtersEnabled
          required: false
          type: string
      responses:
        '200':
          description: Successful Response
  /drug/search/structure/image/:
    parameters: []
    get:
      parameters:
        - in: query
          name: structureId
          required: false
          type: string
        - in: query
          name: drugId
          required: false
          type: string
        - in: query
          name: size
          required: false
          type: string
      responses:
        '200':
          description: Successful Response
  '/drug/search/structure/image/{structureId}':
    parameters:
      - in: path
        name: structureId
        required: true
        type: string
    get:
      parameters:
        - in: query
          name: size
          required: false
          type: string
      responses:
        '200':
          description: Successful Response
  '/drug/search/structure/molfile/{id}':
    parameters:
      - in: path
        name: id
        required: true
        type: string
    get:
      responses:
        '200':
          description: Successful Response
  /drug/search/structure/poll/:
    parameters: []
    get:
      parameters:
        - in: query
          name: token
          required: false
          type: string
      responses:
        '200':
          description: Successful Response
  /drug/sourceSummary:
    parameters: []
    get:
      parameters:
        - in: query
          name: id
          required: false
          type: string
        - in: query
          name: type
          required: false
          type: string
      responses:
        '200':
          description: Successful Response
  /drug/sources:
    parameters: []
    get:
      parameters:
        - in: query
          name: idList
          required: false
          type: string
      responses:
        '200':
          description: Successful Response
  '/drug/sources/{drugId}':
    parameters:
      - in: path
        name: drugId
        required: true
        type: string
    get:
      responses:
        '200':
          description: Successful Response
  '/drug/{id}':
    parameters:
      - in: path
        name: id
        required: true
        type: string
    get:
      parameters:
        - in: query
          name: includeSources
          required: false
          type: string
      responses:
        '200':
          description: Successful Response
  /drugs:
    parameters: []
    get:
      parameters:
        - in: query
          name: idList
          required: false
          type: string
      responses:
        '200':
          description: Successful Response
  /entities:
    parameters: []
    get:
      parameters:
        - in: query
          name: query
          required: false
          type: string
        - in: query
          name: types
          required: false
          type: string
        - in: query
          name: fields
          required: false
          type: string
        - in: query
          name: hits
          required: false
          type: string
        - in: query
          name: linkedTo
          required: false
          type: string
      responses:
        '200':
          description: Successful Response
  '/export/financial/{id}':
    parameters:
      - in: path
        name: id
        required: true
        type: string
    get:
      responses:
        '200':
          description: Successful Response
  '/financial/chart/{id}':
    parameters:
      - in: path
        name: id
        required: true
        type: string
    get:
      responses:
        '200':
          description: Successful Response
  '/financial/{id}':
    parameters:
      - in: path
        name: id
        required: true
        type: string
    get:
      responses:
        '200':
          description: Successful Response
  '/metadata/suported/{version}':
    parameters:
      - in: path
        name: version
        required: true
        type: string
    get:
      responses:
        '200':
          description: Successful Response
  /metadata/version:
    parameters: []
    get:
      responses:
        '200':
          description: Successful Response
  /metadata/versions:
    parameters: []
    get:
      responses:
        '200':
          description: Successful Response
  /search/structure/:
    parameters: []
    post:
      parameters:
        - in: query
          name: query
          required: false
          type: string
        - in: query
          name: offset
          required: false
          type: string
        - in: query
          name: hits
          required: false
          type: string
        - in: query
          name: sortby
          required: false
          type: string
        - in: query
          name: sortBy
          required: false
          type: string
        - in: query
          name: filtersEnabled
          required: false
          type: string
      responses:
        '200':
          description: Successful Response
  '/search/{query}/':
    parameters:
      - in: path
        name: query
        required: true
        type: string
    get:
      parameters:
        - in: query
          name: offset
          required: false
          type: string
        - in: query
          name: hits
          required: false
          type: string
        - in: query
          name: sortby
          required: false
          type: string
        - in: query
          name: sortBy
          required: false
          type: string
        - in: query
          name: filtersEnabled
          required: false
          type: string
        - in: query
          name: querylanguage
          required: false
          type: string
        - in: query
          name: fmt
          required: false
          type: string
      responses:
        '200':
          description: Successful Response
  '/taxonomy/{type}/children/{treecode}':
    parameters:
      - in: path
        name: type
        required: true
        type: string
      - in: path
        name: treecode
        required: true
        type: string
    get:
      parameters:
        - in: query
          name: includedescendants
          required: false
          type: string
        - in: query
          name: enableCounts
          required: false
          type: string
      responses:
        '200':
          description: Successful Response
  '/taxonomy/{type}/parent/{treecode}':
    parameters:
      - in: path
        name: type
        required: true
        type: string
      - in: path
        name: treecode
        required: true
        type: string
    get:
      parameters:
        - in: query
          name: enableCounts
          required: false
          type: string
      responses:
        '200':
          description: Successful Response
  '/taxonomy/{type}/root/':
    parameters:
      - in: path
        name: type
        required: true
        type: string
    get:
      parameters:
        - in: query
          name: enableCounts
          required: false
          type: string
      responses:
        '200':
          description: Successful Response
  '/taxonomy/{type}/search/{searchstring}':
    parameters:
      - in: path
        name: type
        required: true
        type: string
      - in: path
        name: searchstring
        required: true
        type: string
    get:
      parameters:
        - in: query
          name: expandhierarchy
          required: false
          type: string
        - in: query
          name: showDuplicates
          required: false
          type: string
      responses:
        '200':
          description: Successful Response

from elasticsearch.helpers import bulk
from pyelasticsearch import ElasticSearch 

es = ElasticSearch('http://localhost:9200/')

def create_index(index_name,mappings):





def prepare_index_docs(doc_list):
    document_list = [es.index_op(i) for i in doc_list]
    return document_list


def bulk_insertion(index, doc_type, doc_list):
    
    es_docs = prepare_index_docs(doc_list)
    bulk_response = es.bulk(es_docs, doc_type=doc_type, index=index)
    response_items = bulk_response['items']


    
    # for i, item in enumerate(response_items):
    #     if 'create' in item and item['create']['status'] != 201:
    #         print("Failed to parse ")
    #     if 'index' in item  and item['index']['status'] != 201:
    #         print("Error")
        

if __name__ == '__main__':


    
    

    doc_list=[
        {'title': 'title1', 'pages': 20}, {'title': 'title2', 'pages': "hj"},
        {'title': 'title3', 'pages': 20}, {'title': 'title3', 'pages': 20},
        {'title': 'title4', 'pages': 20}
    ]

    for i in range(0,len(doc_list),2):
        try:
            bulk_insertion('library', 'book', doc_list[i:i+2])
        except Exception as e:
            print(e.errors)
            #Todo:  raise error

    

# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # Use a dictionary to store the phone book entries
    phone_book = {}
    for cur_query in queries:
        if cur_query.type == 'add':
            # Add the new entry to the dictionary
            phone_book[cur_query.number] = cur_query.name
        elif cur_query.type == 'del':
            # Remove the entry from the dictionary if it exists
            if cur_query.number in phone_book:
                del phone_book[cur_query.number]
        else:
            # Look up the entry in the dictionary and add the result to the output list
            result.append(phone_book.get(cur_query.number, 'not found'))
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

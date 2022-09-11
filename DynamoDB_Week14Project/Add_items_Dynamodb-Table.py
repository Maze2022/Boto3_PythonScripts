import boto3

dynamodb = boto3.client("dynamodb")

response = dynamodb.batch_write_item(
    RequestItems = {
        "Sports":  [
            {
                "PutRequest": {
                    "Item": {
                        "Name": {
                            "S": "Soccer",
                        },
                        "TopPlayer": {
                            "S": "Christiano Ronaldo",
                        },
                        "Ranking": {
                            "N": '1',
                        },
                        "Fans": {
                            "S": "4 billion",
                        },
                    },
                },
            },
            {
                "PutRequest": {
                    "Item": {
                        "Name": {
                            "S": "Cricket",
                        },
                       "TopPlayer": {
                            "S": "Babar Azam",
                        },
                        "Ranking": {
                            "N": '2',
                        },
                        "Fans": {
                            "S": "2.5 billion",
                        },
                    },
                },
            },
            {
                "PutRequest": {
                    "Item": {
                        "Name": {
                            "S": "Hockey",
                        },
                       "TopPlayer": {
                            "S": "Connor McDavid",
                        },
                        "Ranking": {
                            "N": '3',
                        },
                        "Fans": {
                            "S": "2 Billion",
                        },
                    },
                },
            },
            {
                "PutRequest": {
                    "Item": {
                        "Name": {
                            "S": "Tennis",
                        },
                       "TopPlayer": {
                            "S": "Daniil Medvedev",
                        },
                        "Ranking": {
                            "N": '4',
                        },
                        "Fans": {
                            "S": "1 billion",
                        },
                    },
                },

            },
            {
                
                "PutRequest": {
                    "Item": {
                        "Name": {
                            "S": "Volleyball",
                        },
                       "TopPlayer": {
                            "S": "Ivan Zaytsez",
                        },
                        "Ranking": {
                            "N": '5',
                        },
                        "Fans": {
                            "S": "900 million",
                        },
                    },
                },
            },
            {
                "PutRequest": {
                    "Item": {
                        "Name": {
                            "S": "Table Tennis",
                        },
                       "TopPlayer": {
                            "S": "Fan Zhendong",
                        },
                        "Ranking": {
                            "N": '6',
                        },
                        "Fans": {
                            "S": "875 million"
                        },
                    },
                },
            },
            {
                "PutRequest": {
                    "Item": {
                        "Name": {
                            "S": "Basketball"
                        },
                       "TopPlayer": {
                            "S": "Giannis Antetokounmpo"
                        },
                        "Ranking": {
                            "N": '7',
                        },
                        "Fans": {
                            "S": "825 million"
                        },
                    },
                },
            },
            {
                "PutRequest": {
                    "Item": {
                        "Name": {
                            "S": "Baseball"
                        },
                       "TopPlayer": {
                            "S": "Aaron Judge"
                        },
                        "Ranking": {
                            "N": '8',
                        },
                        "Fans": {
                            "S": "500 million"
                        },
                    },
                },
            },
             {
                "PutRequest": {
                    "Item": {
                        "Name": {
                            "S": "Rugby"
                        },
                       "TopPlayer": {
                            "S": "Antoine Dupont"
                        },
                        "Ranking": {
                            "N": '9',
                        },
                        "Fans": {
                            "S": "475 million"
                        },
                    },
                },
            },
            {
                "PutRequest": {
                    "Item": {
                        "Name": {
                            "S": "Golf"
                        },
                       "TopPlayer": {
                            "S": "Scottie Scheffler"
                        },
                        "Ranking": {
                            "N": '10',
                        },
                        "Fans": {
                            "S": "450 million"
                        },
                    },
                },
            },
        ],
    },
)

print(response)
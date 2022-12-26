import json
import uuid
import copy

g_res  = None
with open("C:\\Users\\Administrator\\Desktop\\test1.pygraph") as fp:
    g_res = json.load(fp)


nodeAttribute = {
    "SourceNode": {
        "package": "InsituPackage",
        "lib":None,
        "type": "SourceNode",
        "owningGraphName": "root",
        "name": "SourceNode",
        "uuid": "ec851cb3-9702-4a47-84ab-e5e25327e197",
        "inputs": [],
        "outputs": [
            {
                "name": "out",
                "package": "InsituPackage",
                "fullName": "SourceNode_out",
                "dataType": "NumpyDataPin",
                "direction": 1,
                "value": None,
                "uuid": "f156f5b3-3584-4724-8c5d-c88244be139a",
                "linkedTo": [
                    {
                        "lhsNodeName": "SourceNode",
                        "outPinId": 1,
                        "rhsNodeName": "VertifyNode",
                        "inPinId": 1,
                        "lhsNodeUid": "ec851cb3-9702-4a47-84ab-e5e25327e197",
                        "rhsNodeUid": "2288304e-461d-416b-ae9a-84f42be0484c"
                    }
                ],
                "pinIndex": 1,
                "options": [],
                "structure": 0,
                "alwaysList": False,
                "alwaysSingle": False,
                "alwaysDict": False,
                "wrapper":{
                    "bLabelHidden": False,
                    "displayName": "out",
                    "wires": {
                        "1": {
                            "sourceUUID": "f156f5b3-3584-4724-8c5d-c88244be139a",
                            "destinationUUID": "fe88bd1a-dd6a-4451-b741-550f141ed80c",
                            "sourceName": "SourceNode_out",
                            "destinationName": "VertifyNode_inp1",
                            "uuid": "255eadc0-9380-46d7-aeba-6f27e0cde386",
                            "hOffsetL": "0.0",
                            "hOffsetR": "0.0",
                            "hOffsetLSShape": "0.0",
                            "hOffsetRSShape": "0.0",
                            "vOffset": "0.0",
                            "vOffsetSShape": "0.0",
                            "snapVToFirst": 1,
                            "snapVToSecond": 0
                        }
                    }
                },
            }
        ],
        "meta": {
            "var": {},
            "label": "SourceNode"
        },
        "wrapper":{
            "collapsed": False,
            "headerHtml": "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\np, li { white-space: pre-wrap; }\n</style></head><body style=\" font-family:'Consolas'; font-size:6pt; font-weight:400; font-style:normal;\">\n<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">SourceNode</p></body></html>",
            "exposeInputsToCompound": False,
            "groups": {
                "input": {},
                "output": {}
            }
        },
        "x": -672.0,
        "y": 108.0
    },
    "VertifyNode": {
        "package": "InsituPackage",
        "lib": None,
        "type": "VertifyNode",
        "owningGraphName": "root",
        "name": "VertifyNode",
        # 需要初始化
        "uuid": "2288304e-461d-416b-ae9a-84f42be0484c",
        "inputs": [
            {
                "name": "inp1",
                "package": "InsituPackage",
                "fullName": "VertifyNode_inp1",
                "dataType": "NumpyDataPin",
                "direction": 0,
                # 运行中赋值
                "value": None,
                # 需要初始化
                "uuid": "fe88bd1a-dd6a-4451-b741-550f141ed80c",
                # 构建连接关系
                "linkedTo": [
                    {
                        "lhsNodeName": "SourceNode",
                        "outPinId": 1,
                        "rhsNodeName": "VertifyNode",
                        "inPinId": 1,
                        "lhsNodeUid": "ec851cb3-9702-4a47-84ab-e5e25327e197",
                        "rhsNodeUid": "2288304e-461d-416b-ae9a-84f42be0484c"
                    }
                ],
                "pinIndex": 1,
                "options": [],
                "structure": 0,
                "alwaysList": False,
                "alwaysSingle": False,
                "alwaysDict": False,
                # TODO
                "wrapper":{
                    "bLabelHidden": False,
                    "displayName": "inp1",
                    "wires": {
                        "1": {
                            "sourceUUID": "f156f5b3-3584-4724-8c5d-c88244be139a",
                            "destinationUUID": "fe88bd1a-dd6a-4451-b741-550f141ed80c",
                            "sourceName": "SourceNode_out",
                            "destinationName": "VertifyNode_inp1",
                            "uuid": "255eadc0-9380-46d7-aeba-6f27e0cde386",
                            "hOffsetL": "0.0",
                            "hOffsetR": "0.0",
                            "hOffsetLSShape": "0.0",
                            "hOffsetRSShape": "0.0",
                            "vOffset": "0.0",
                            "vOffsetSShape": "0.0",
                            "snapVToFirst": 1,
                            "snapVToSecond": 0
                        }
                    }
                }
            },
        ],
        "outputs": [
                {
                    "name": "out1",
                    "package": "InsituPackage",
                    "fullName": "VertifyNode_out1",
                    "dataType": "NumpyDataPin",
                    "direction": 1,
                    "value": None,
                    "uuid": "",
                    "linkedTo": [
                        {
                            "lhsNodeName": "VertifyNode",
                            "outPinId": 1,
                            "rhsNodeName": "consoleOutput",
                            "inPinId": 2,
                            "lhsNodeUid": "2288304e-461d-416b-ae9a-84f42be0484c",
                            "rhsNodeUid": "083d03f0-e2f0-4426-89cb-addaafe83785"
                        }
                    ],
                    "pinIndex": 1,
                    "options": [],
                    "structure": 0,
                    "alwaysList": False,
                    "alwaysSingle": False,
                    "alwaysDict": False,
                    "wrapper": {
                        "bLabelHidden": False,
                        "displayName": "out1",
                        "wires": {
                            "2": {
                                "sourceUUID": "867d2eda-ae35-4b5e-a494-f75c29ac3572",
                                "destinationUUID": "0d0c23e9-686e-4a36-ad7d-c71f5df83330",
                                "sourceName": "VertifyNode_out1",
                                "destinationName": "consoleOutput_entity",
                                "uuid": "11467bfc-3354-4e9d-ac84-59ba40e54c25",
                                "hOffsetL": "0.0",
                                "hOffsetR": "0.0",
                                "hOffsetLSShape": "0.0",
                                "hOffsetRSShape": "0.0",
                                "vOffset": "0.0",
                                "vOffsetSShape": "0.0",
                                "snapVToFirst": 1,
                                "snapVToSecond": 0
                            }
                        }
                    }
                }
            ],
            "meta": {
                "var": {},
                "label": "VertifyNode"
            },
            "wrapper": {
                "collapsed": False,
                "headerHtml": "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\np, li { white-space: pre-wrap; }\n</style></head><body style=\" font-family:'Consolas'; font-size:6pt; font-weight:400; font-style:normal;\">\n<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">VertifyNode</p></body></html>",
                "exposeInputsToCompound": False,
                "groups": {
                    "input": {},
                    "output": {}
                }
            },
            "x": -435.0,
            "y": 117.0
    },
    "consoleOutput": {
        "package": "PyFlowBase",
        "lib": None,
        "type": "consoleOutput",
        "owningGraphName": "root",
        "name": "consoleOutput",
        "uuid": "083d03f0-e2f0-4426-89cb-addaafe83785",
        "inputs": [
            {
                "name": "entity",
                "package": "PyFlowBase",
                "fullName": "consoleOutput_entity",
                "dataType": "AnyPin",
                "direction": 0,
                "value": "None",
                "uuid": "0d0c23e9-686e-4a36-ad7d-c71f5df83330",
                "linkedTo": [
                    {
                        "lhsNodeName": "VertifyNode",
                        "outPinId": 1,
                        "rhsNodeName": "consoleOutput",
                        "inPinId": 2,
                        "lhsNodeUid": "2288304e-461d-416b-ae9a-84f42be0484c",
                        "rhsNodeUid": "083d03f0-e2f0-4426-89cb-addaafe83785"
                    }
                ],
                "pinIndex": 2,
                "options": [
                    16,
                    256,
                    512
                ],
                "structure": 0,
                "alwaysList": False,
                "alwaysSingle": False,
                "alwaysDict": False,
                "wrapper": {
                    "bLabelHidden": False,
                    "displayName": "entity",
                    "wires": {
                        "2": {
                            "sourceUUID": "867d2eda-ae35-4b5e-a494-f75c29ac3572",
                            "destinationUUID": "0d0c23e9-686e-4a36-ad7d-c71f5df83330",
                            "sourceName": "VertifyNode_out1",
                            "destinationName": "consoleOutput_entity",
                            "uuid": "11467bfc-3354-4e9d-ac84-59ba40e54c25",
                            "hOffsetL": "0.0",
                            "hOffsetR": "0.0",
                            "hOffsetLSShape": "0.0",
                            "hOffsetRSShape": "0.0",
                            "vOffset": "0.0",
                            "vOffsetSShape": "0.0",
                            "snapVToFirst": 1,
                            "snapVToSecond": 0
                        }
                    }
                },
                "currDataType": "NumpyDataPin"
            },
            {
                "name": "inExec",
                "package": "PyFlowBase",
                "fullName": "consoleOutput_inExec",
                "dataType": "ExecPin",
                "direction": 0,
                "value": "None",
                "uuid": "34ea5508-b213-479f-a037-c07800615023",
                "linkedTo": [],
                "pinIndex": 1,
                "options": [
                    8,
                    256
                ],
                "structure": 0,
                "alwaysList": False,
                "alwaysSingle": False,
                "alwaysDict": False,
                "wrapper": {
                    "bLabelHidden": False,
                    "displayName": "inExec",
                    "wires": {}
                }
            }
        ],
        "outputs": [
            {
                "name": "outExec",
                "package": "PyFlowBase",
                "fullName": "consoleOutput_outExec",
                "dataType": "ExecPin",
                "direction": 1,
                "value": "None",
                "uuid": "8722c984-dce4-4abf-9512-c2bf861e761e",
                "linkedTo": [],
                "pinIndex": 1,
                "options": [
                    256
                ],
                "structure": 0,
                "alwaysList": False,
                "alwaysSingle": False,
                "alwaysDict": False,
                "wrapper": {
                    "bLabelHidden": False,
                    "displayName": "outExec",
                    "wires": {}
                }
            }
        ],
        "meta": {
            "var": {},
            "label": "consoleOutput"
        },
        "wrapper": {
        },
        "x": -172.0,
        "y": 138.0
    },

}



def convert(inputData: list):
    print(inputData)
    res = {
        "name": "root",
        "category": "",
        "vars": [],
        "nodes":[],
        "depth": 1,
        "isRoot": True,
        "parentGraphName": "None",
        "fileVersion": "2.0.1",
        "activeGraph": "root"
    }
    print("初始化完成")
    # 临时存储节点
    nodes = {}
    
    for item in inputData:
        # 生成节点，每个节点对应唯一的uuid
        for key in item:
            if key != "port" and item[key] not in nodes:
                nodeName = item[key]
                # print(nodeName)
                node = copy.deepcopy(nodeAttribute[nodeName])
                # 生成唯一的uuid
                node_uuid = uuid.uuid1()
                if not node["uuid"]:
                    node["uuid"] = node_uuid
                if nodeName not in nodes:
                    nodes[nodeName] = node
    for item in inputData:
        for key in item:
            # 生成DAG图的连接关系
            newLinkTo = {
                # 左节点
                "lhsNodeName": item['src'],
                "outPinId": 1,
                # 右节点
                "rhsNodeName": item['dest'],
                "inPinId": 1,
                "lhsNodeUid": nodes[item['src']]['uuid'],
                "rhsNodeUid": nodes[item['dest']]['uuid']
            }
            # 通过uuid绑定左右节点的连接关系
            if  nodes[item['src']]['outputs'] is not None:
                nodes[item['src']]['outputs'].append(newLinkTo)
            if nodes[item['dest']]['inputs'] is not None:
                nodes[item['dest']]['outputs'].append(newLinkTo)
    res["nodes"] = nodes

    with open("test3.pygraph", "w") as f:
        dic_to_json = json.dumps(g_res)
        f.write(dic_to_json)



if __name__ == "__main__":
    exam = [
        {
            "src": "SourceNode",
            "dest": "VertifyNode"
        },
        {
            "src": "VertifyNode",
            "dest": "consoleOutput"
        },
    ]
    convert(exam)

# -*- coding: utf-8 -*-
import datetime
version = '3.2.0'
plugins = [
{'plugintype': 'channel', 'apop': False, 'archivepath': '', 'askmdn': 'no', 'certfile': None, 'charset': 'us-ascii', 'desc': None, 'filename': '*.edi', 'ftpaccount': '', 'ftpactive': False, 'ftpbinary': False, 'host': '', 'idchannel': 'myfirstroute_in', 'inorout': 'in', 'keyfile': None, 'lockname': '', 'mdnchannel': '', 'parameters': '', 'path': 'botssys/infile/my_first_plugin', 'port': 0, 'remove': False, 'rsrv1': None, 'rsrv2': None, 'rsrv3': None, 'secret': '', 'sendmdn': 'no', 'starttls': False, 'syslock': False, 'testpath': '', 'type': 'file', 'username': ''},
{'plugintype': 'channel', 'apop': False, 'archivepath': '', 'askmdn': 'no', 'certfile': None, 'charset': 'us-ascii', 'desc': None, 'filename': 'orders*.inh', 'ftpaccount': '', 'ftpactive': False, 'ftpbinary': False, 'host': '', 'idchannel': 'myfirstroute_out', 'inorout': 'out', 'keyfile': None, 'lockname': '', 'mdnchannel': '', 'parameters': '', 'path': 'botssys/outfile/my_first_plugin', 'port': 0, 'remove': False, 'rsrv1': None, 'rsrv2': None, 'rsrv3': None, 'secret': '', 'sendmdn': 'no', 'starttls': False, 'syslock': False, 'testpath': '', 'type': 'file', 'username': ''},
{'plugintype': 'translate', 'active': True, 'alt': '', 'desc': None, 'fromeditype': 'edifact', 'frommessagetype': 'ORDERSD96AUNEAN008', 'frompartner': None, 'rsrv1': None, 'rsrv2': None, 'toeditype': 'fixed', 'tomessagetype': 'ordersfixed', 'topartner': None, 'tscript': 'myfirstscriptordersedi2fixed'},
{'plugintype': 'routes', 'active': True, 'alt': '', 'defer': False, 'desc': None, 'fromchannel': 'myfirstroute_in', 'fromeditype': 'edifact', 'frommessagetype': 'edifact', 'frompartner': None, 'frompartner_tochannel': None, 'idroute': 'myfirstroute', 'notindefaultrun': False, 'rsrv1': None, 'rsrv2': None, 'seq': 9999, 'testindicator': '', 'tochannel': 'myfirstroute_out', 'toeditype': '', 'tomessagetype': '', 'topartner': None, 'topartner_tochannel': None, 'translateind': 1, 'zip_incoming': None, 'zip_outgoing': None},
]
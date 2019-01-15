import json
import requests as req

class elastic_client():
	
	def __init__(self, uri=None, headers=None, username=None, password=None):
		self.uri = uri
		self.headers = headers		
		self.username = username
		self.password = password
		return
##################################################################################################
# End __init__()
##################################################################################################
	def get_timeseries(self, data):
		'''Function to get timeseries data from ElasticSearch for an endpoint and parse results
		Parameters
		----------
		data : string
		String composed of metrics to find exact point in ElasticSearch

		Returns
		-------
		returned_dict : dictionary
		Dictionary of parsed timesereis information with Tree structure of {value -> [[DateTime,Data]*]}
		
		'''
		
		returned_dict = {}
		try:
			ret = req.post(self.uri, headers=self.headers,auth=(self.username,self.password),data=data)
			var = json.loads(ret.json())
			value_list = []
			for item in var['value']:
				value_list.append([item[0],item[1]])
				#datum.append(item[1])
				#timestamp.append(item[0])
			returned_dict["value"] = value_list
			
		except Exception as e:
			print("Error getting meter data: ",str(e))

		return returned_dict
##################################################################################################
# End get_timeseries()
##################################################################################################

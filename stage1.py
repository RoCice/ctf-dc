import requests
from env import config
import json
from utils.auth import IntersightAuth
from pprint import pprint

def getAlarmsDescription():
    """Extract the descriptions of alarms

    Returns
    ----------
    alarms_description:
        json format of the description of the alarms

    Raises
    -------
    NotImplementedError
        a list of strings used that are the header columns
    """

    try:
        auth=IntersightAuth(secret_key_filename=config['INTERSIGHT_CERT'], api_key_id=config['INTERSIGHT_API_KEY'])
        BASE_URL='https://www.intersight.com/api/v1'
        url = f"{BASE_URL}/cond/Alarms"

        response = requests.get(url, auth=auth)
        alarms_description = response.json()

        return alarms_description

    except:
        raise NotImplementedError("Silent Animals are not supported!")

def getSummaryPhysicalInfrastructure():
    """Retrieve a summary of the physical infrastructure

    Returns
    ----------
    infrastructure_summary: list
        a list containing Management Mode, Management IP, Name, CPUs, Cores, PowerState, Firmware, Model, 
        Serial and License Tier

    Raises
    -------
    NotImplementedError
        a list of strings used that are the header columns
    """

    try:
        auth=IntersightAuth(secret_key_filename=config['INTERSIGHT_CERT'], api_key_id=config['INTERSIGHT_API_KEY'])
        BASE_URL='https://www.intersight.com/api/v1'
        url = f"{BASE_URL}/compute/PhysicalSummaries"

        response = requests.get(url, auth=auth)
        testData = response.json()
        infrastructure_summary = []

        for data in testData["Results"]:

            mgmtModes = data["ManagementMode"]
            mgmtIPs = data["MgmtIpAddress"]
            names = data["Name"]
            cpus = data["NumCpus"]
            cpuCores = data["NumCpuCores"]
            powerStates = data["OperPowerState"]
            firmwares = data["Firmware"]
            models = data["Model"]
            serials = data["Moid"]

            dictTempo = {"mgmtModes": mgmtModes, "mgmtIPs": mgmtIPs, "names": names, "cpus": cpus, "cpuCores": cpuCores, "powerStates": powerStates, "firmwares": firmwares, "models": models, "serials": serials}
            infrastructure_summary.append(dictTempo)

        #return response.json()
        return infrastructure_summary

    except:
        raise NotImplementedError("Physical infrastructures are not supported!")



def getVendorInfoComplianceHCL(vendorMoid):
    """Retrieve OS Vendor and OS Version

    Returns
    ----------
    os_vendors
        return os vendor and os version 

    Raises
    -------
    NotImplementedError
        If no compliance with HCL
    """

    try:
        auth=IntersightAuth(secret_key_filename=config['INTERSIGHT_CERT'], api_key_id=config['INTERSIGHT_API_KEY'])
        BASE_URL='https://www.intersight.com/api/v1'
        url = f"{BASE_URL}/hcl/OperatingSystemVendors/{vendorMoid}"

        response = requests.get(url, auth=auth)
        os_vendors = response.json()
        
        return os_vendors
    
    except:
        raise NotImplementedError("Compliance with Hardware Compatibility List (HCL) is not supported!")



def getComplianceHCL():
    """Retrieve OS Vendor and OS Version

    Returns
    ----------
    os_vendors
        return os vendor and os version 

    Raises
    -------
    NotImplementedError
        If no compliance with HCL
    """

    try:
        auth=IntersightAuth(secret_key_filename=config['INTERSIGHT_CERT'], api_key_id=config['INTERSIGHT_API_KEY'])
        BASE_URL='https://www.intersight.com/api/v1'
        url = f"{BASE_URL}/hcl/OperatingSystems"

        response = requests.get(url, auth=auth)
        testData = response.json()
        responseSummary = []

        for data in testData["Results"]:

            version = data["Version"]
            vendorMoid = data["Vendor"]["Moid"]

            dictTempo = {"version": version, "vendorMoid": vendorMoid}
            responseSummary.append(dictTempo)

        #return response.json()
        return responseSummary

    except:
        raise NotImplementedError("Silent Animals are not supported!")

def getListNameKubernetesCluster():
    """Retrieve an overview of all kubernetes clusters running on this cluster

    Returns
    ----------
    kubernetes_cluster_names
        return names of all kubernetes clusters running on this cluster

    Raises
    -------
    NotImplementedError
        If no kubernetes cluster is running on this cluster
    """

    try:
        auth=IntersightAuth(secret_key_filename=config['INTERSIGHT_CERT'], api_key_id=config['INTERSIGHT_API_KEY'])
        BASE_URL='https://www.intersight.com/api/v1'
        url = f"{BASE_URL}/kubernetes/ClusterProfiles"

        response = requests.get(url, auth=auth)
        testData = response.json()
        kubernetes_cluster_names = []

        for data in testData["Results"]:

            name = data["Name"]

            kubernetes_cluster_names.append(name)

        #return response.json()
        return kubernetes_cluster_names

    except:
        raise NotImplementedError("Kubernetes Clusters are not supported!")

def getCountKubernetesCluster():
    """Retrieve an overivew of deployments running in the kubernetes cluster

    Returns
    ----------
    kubernetes_cluster_count
        return the number of deployments running in the kubernetes cluster

    Raises
    -------
    NotImplementedError
        If no kubernetes cluster is running on this cluster
    """

    try:
        kubernetes_cluster = getListNameKubernetesCluster()
        kubernetes_cluster_count = len(kubernetes_cluster)
        return kubernetes_cluster_count

    except:
        raise NotImplementedError("Kubernetes clusters are not set and supported!")

def main():

    getAlarmsDescription()
    getSummaryPhysicalInfrastructure()
    getComplianceHCL()
    getListNameKubernetesCluster()
    test_req = getCountKubernetesCluster()
    pprint(test_req, indent=6)

if __name__ == "__main__":
    # execute only if run as a script
    main()
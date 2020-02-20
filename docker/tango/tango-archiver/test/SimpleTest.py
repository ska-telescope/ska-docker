import tango
from tango import DevFailed, DeviceProxy, GreenMode, AttributeProxy
import time
from time import sleep
import pytest
import logging

def test_cm_device_is_ON():
    tango_test = tango.DeviceProxy("archiving/hdbpp/confmanager01")
    time.sleep(2)
    assert tango_test.state() == tango.DevState.ON

def test_es_device_is_ON():
    tango_test = tango.DeviceProxy("archiving/hdbpp/eventsubscriber01")
    time.sleep(2)
    assert tango_test.state() == tango.DevState.ON

def test_archiving():
  evt_subscriber_device_fqdn = "archiving/hdbpp/eventsubscriber01"
  config_manager_device_fqdn = "archiving/hdbpp/confmanager01"
  conf_manager_proxy = DeviceProxy(config_manager_device_fqdn)
  evt_subscriber_device_proxy = DeviceProxy(evt_subscriber_device_fqdn)

  conf_manager_proxy.set_timeout_millis(5000)
  evt_subscriber_device_proxy.set_timeout_millis(5000)

  attribute = "sys/tg_test/1/double_scalar"

  # wait for the attribute to be online. 
  max_retries = 10
  sleep_time = 30
  for x in range(0, max_retries):
      try:
        att = AttributeProxy(attribute)
        att.read()
        break
      except DevFailed as df:
        if(x == (max_retries -1)):
          raise df
        logging.info("DevFailed exception: " + str(df.args[0].reason) + ". Sleeping for " + str(sleep_time) + "ss")
        sleep(sleep_time)

  conf_manager_proxy.write_attribute("SetAttributeName", attribute)
  conf_manager_proxy.write_attribute("SetArchiver", evt_subscriber_device_fqdn)
  conf_manager_proxy.write_attribute("SetStrategy", "ALWAYS")
  conf_manager_proxy.write_attribute("SetPollingPeriod", 1000)
  conf_manager_proxy.write_attribute("SetPeriodEvent", 3000)

  try:
    conf_manager_proxy.command_inout("AttributeAdd")
  except DevFailed as df:
    if not str(df.args[0].reason) == 'Already archived':    
      logging.info("DevFailed exception: " + str(df.args[0].reason))

  evt_subscriber_device_proxy.Start()

  max_retries = 10
  sleep_time = 1
  for x in range(0, max_retries):
    try:
      # Check status of Attribute Archiving in Configuration Manager
      result_config_manager = conf_manager_proxy.command_inout("AttributeStatus", attribute)
      # Check status of Attribute Archiving in Event Subscriber
      result_evt_subscriber = evt_subscriber_device_proxy.command_inout("AttributeStatus", attribute)
      assert "Archiving          : Started" in result_config_manager
      assert "Archiving          : Started" in result_evt_subscriber
    except DevFailed as df:
      if(x == (max_retries -1)):
        raise df
      logging.info("DevFailed exception: " + str(df.args[0].reason) + ". Sleeping for " + str(sleep_time) + "ss")
      sleep(sleep_time)

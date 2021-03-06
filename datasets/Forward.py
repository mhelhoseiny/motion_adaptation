from Forwarding.Forwarder import ImageForwarder
from Forwarding.BaseForwarder import BaseForwarder
from Forwarding.OneshotForwarder import OneshotForwarder
from Forwarding.TeacherAdaptingForwarder import TeacherAdaptingForwarder
from Forwarding.TeacherContAdaptingForwarder import TeacherContAdaptingForwarder
from Forwarding.UnsupervisedForwarder import UnsupervisedForwarder


def forward(engine, network, data, dataset_name, save_results, save_logits):
  forwarder = ImageForwarder(engine)
  forwarder.forward(network, data, save_results, save_logits)


def base_forward(engine, save_results, save_logits):
  if engine.dataset in ("davis"):
#    forwarder = BaseForwarder(engine)
    forwarder = UnsupervisedForwarder(engine)
  else:
    assert False, "unknown dataset for oneshot: " + engine.dataset
  forwarder.forward(None, None, save_results, save_logits)


def online_forward(engine, save_results, save_logits):
  forwarder = TeacherAdaptingForwarder(engine)
  forwarder.forward(None, None, save_results, save_logits)

def online_forward_cont(engine, save_results, save_logits):
  forwarder = TeacherContAdaptingForwarder(engine)
  forwarder.forward(None, None, save_results, save_logits)

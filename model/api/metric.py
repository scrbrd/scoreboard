""" Module: metric

Each metric is a type of measurement that can be used for a Game. ResultMetric
is stored as an EDGE_TYPE but the rest of the metrics are stored as Edge
Properties.

MetricFactory converts a metric dictionary into a Metric list.

"""
from util.decorators import constant

from constants import API_EDGE_TYPE
from exceptions import InputError


class _MetricType(object):

    """ Constants for all the metric types. """


    @constant
    def RESULT(self):
        """ RESULT is a metric type. """
        return "result"


METRIC_TYPE = _MetricType()


class Metric(object):

    """ Metric is a generic measurement for Games and Opponents.

    Required:
    str     _type       the type of result

    """


    def __init__(self, metric_value):
        """ Construct an abstract Metric. """
        raise NotImplementedError("Subclass Metric and Override!")


    @property
    def type(self):
        """ Return the type of Metric. """
        # TODO: util.assert_loaded(self._type)
        return self._type


class MetricFactory(object):

    """ MetricFactory turns dictionaries of metrics into Metric objects. """


    @staticmethod
    def produce_metrics(metric_dict):
        """ Produce a dictionary of Metrics.

        Return a list of Metric objects.

        """
        metric_objects = []
        for metric_type, metric_value in metric_dict.items():
            if metric_type == METRIC_TYPE.RESULT:
                metric_objects.append(ResultMetric(metric_value))
            else:
                raise InputError("Metric Type", metric_type)

        return metric_objects


class DiscreteMetric(Metric):

    """ DiscreteMetric is a measurement with a list of possible values.

    Optional:
    list    _values     an optional list of values for a metric.

    """


    @property
    def values(self):
        """ Return a list of values for this Metric."""
        # TODO: Metric.assert_loaded(self._values)
        return self._values


class ResultMetric(DiscreteMetric):

    """ ResultMetric is the result of a Game.

    Required:
    str     _result     the result of a game.

    """


    def __init__(self, result):
        """ Construct a ResultMetric.

        Required:
        str     result      A Game's result.

        """
        self._type = METRIC_TYPE.RESULT
        self._values = [
                API_EDGE_TYPE.WON,
                API_EDGE_TYPE.LOST,
                API_EDGE_TYPE.TIED,
                API_EDGE_TYPE.PLAYED
                ]
        self._result = result

        if result not in self._values:
            raise InputError("Result", result)


    @property
    def result(self):
        """ Return the result of the Game. """
        return self._result

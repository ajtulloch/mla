# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protobufs/ml.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protobufs/ml.proto',
  package='mlappliance',
  serialized_pb='\n\x12protobufs/ml.proto\x12\x0bmlappliance\"5\n\x12OnlineTrainRequest\x12\x10\n\x08\x66\x65\x61tures\x18\x01 \x03(\x01\x12\r\n\x05label\x18\x02 \x01(\x08\"\x15\n\x13OnlineTrainResponse\"(\n\x14OnlinePredictRequest\x12\x10\n\x08\x66\x65\x61tures\x18\x01 \x03(\x01\"+\n\x15OnlinePredictResponse\x12\x12\n\nprediction\x18\x01 \x01(\x01\"{\n\x0cTrainingData\x12\'\n\x06source\x18\x01 \x01(\x0e\x32\x17.mlappliance.DataSource\x12\x33\n\ninlineData\x18\x02 \x03(\x0b\x32\x1f.mlappliance.OnlineTrainRequest\x12\r\n\x05s3URL\x18\x03 \x01(\t\"D\n\x11\x42\x61tchTrainRequest\x12/\n\x0ctrainingData\x18\x01 \x01(\x0b\x32\x19.mlappliance.TrainingData\"\xa2\t\n\x05Model\x12/\n\talgorithm\x18\x01 \x01(\x0e\x32\x1c.mlappliance.Model.Algorithm\x12\x31\n\nparameters\x18\x02 \x01(\x0b\x32\x1d.mlappliance.Model.Parameters\x12G\n\x15performanceStatistics\x18\x03 \x01(\x0b\x32(.mlappliance.Model.PerformanceStatistics\x12\x41\n\x12\x66\x65\x61tureImportances\x18\x04 \x01(\x0b\x32%.mlappliance.Model.FeatureImportances\x12\x31\n\nserialized\x18\x05 \x01(\x0b\x32\x1d.mlappliance.Model.Serialized\x1ax\n\nParameters\x12@\n\x0fhyperParameters\x18\x01 \x03(\x0b\x32\'.mlappliance.Model.Parameters.Parameter\x1a(\n\tParameter\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01\x1a\xb0\x03\n\x15PerformanceStatistics\x12\x45\n\x07metrics\x18\x01 \x03(\x0b\x32\x34.mlappliance.Model.PerformanceStatistics.Performance\x12\x43\n\x08rocCurve\x18\x02 \x03(\x0b\x32\x31.mlappliance.Model.PerformanceStatistics.ROCPoint\x1a]\n\x0bPerformance\x12?\n\x06metric\x18\x01 \x01(\x0e\x32/.mlappliance.Model.PerformanceStatistics.Metric\x12\r\n\x05score\x18\x02 \x01(\x01\x1a?\n\x08ROCPoint\x12\x19\n\x11\x66\x61lsePositiveRate\x18\x01 \x01(\x01\x12\x18\n\x10truePositiveRate\x18\x02 \x01(\x01\"k\n\x06Metric\x12\x0c\n\x08\x41\x43\x43URACY\x10\x01\x12\x15\n\x11\x41VERAGE_PRECISION\x10\x02\x12\x06\n\x02\x46\x31\x10\x03\x12\x0c\n\x08LOG_LOSS\x10\x04\x12\r\n\tPRECISION\x10\x05\x12\n\n\x06RECALL\x10\x06\x12\x0b\n\x07ROC_AUC\x10\x07\x1a\x9c\x01\n\x12\x46\x65\x61tureImportances\x12L\n\x0bimportances\x18\x01 \x03(\x0b\x32\x37.mlappliance.Model.FeatureImportances.FeatureImportance\x1a\x38\n\x11\x46\x65\x61tureImportance\x12\x0f\n\x07\x66\x65\x61ture\x18\x01 \x01(\x03\x12\x12\n\nimportance\x18\x02 \x01(\x01\x1a\x37\n\nSerialized\x12\x15\n\rpickledString\x18\x01 \x01(\x0c\x12\x12\n\njsonString\x18\x02 \x01(\t\"q\n\tAlgorithm\x12\x17\n\x13LOGISTIC_REGRESSION\x10\x01\x12\x14\n\x10GRADIENT_BOOSTED\x10\x02\x12\x12\n\x0eRANDOM_FORESTS\x10\x03\x12\x0e\n\nLINEAR_SVM\x10\x04\x12\x11\n\rNONLINEAR_SVM\x10\x05\"\xbe\x01\n\x0eTrainingReport\x12H\n\x11summaryStatistics\x18\x02 \x01(\x0b\x32-.mlappliance.TrainingReport.SummaryStatistics\x12\"\n\x06models\x18\x03 \x03(\x0b\x32\x12.mlappliance.Model\x1a>\n\x11SummaryStatistics\x12\x13\n\x0bnumExamples\x18\x01 \x01(\x03\x12\x14\n\x0cnumPositives\x18\x02 \x01(\x03**\n\nDataSource\x12\n\n\x06INLINE\x10\x01\x12\x06\n\x02S3\x10\x02\x12\x08\n\x04HDFS\x10\x03')

_DATASOURCE = _descriptor.EnumDescriptor(
  name='DataSource',
  full_name='mlappliance.DataSource',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INLINE', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S3', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HDFS', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1777,
  serialized_end=1819,
)

DataSource = enum_type_wrapper.EnumTypeWrapper(_DATASOURCE)
INLINE = 1
S3 = 2
HDFS = 3


_MODEL_PERFORMANCESTATISTICS_METRIC = _descriptor.EnumDescriptor(
  name='Metric',
  full_name='mlappliance.Model.PerformanceStatistics.Metric',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ACCURACY', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AVERAGE_PRECISION', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='F1', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOG_LOSS', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRECISION', index=4, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RECALL', index=5, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROC_AUC', index=6, number=7,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1144,
  serialized_end=1251,
)

_MODEL_ALGORITHM = _descriptor.EnumDescriptor(
  name='Algorithm',
  full_name='mlappliance.Model.Algorithm',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LOGISTIC_REGRESSION', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GRADIENT_BOOSTED', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RANDOM_FORESTS', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LINEAR_SVM', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NONLINEAR_SVM', index=4, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1469,
  serialized_end=1582,
)


_ONLINETRAINREQUEST = _descriptor.Descriptor(
  name='OnlineTrainRequest',
  full_name='mlappliance.OnlineTrainRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='features', full_name='mlappliance.OnlineTrainRequest.features', index=0,
      number=1, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='label', full_name='mlappliance.OnlineTrainRequest.label', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=35,
  serialized_end=88,
)


_ONLINETRAINRESPONSE = _descriptor.Descriptor(
  name='OnlineTrainResponse',
  full_name='mlappliance.OnlineTrainResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=90,
  serialized_end=111,
)


_ONLINEPREDICTREQUEST = _descriptor.Descriptor(
  name='OnlinePredictRequest',
  full_name='mlappliance.OnlinePredictRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='features', full_name='mlappliance.OnlinePredictRequest.features', index=0,
      number=1, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=113,
  serialized_end=153,
)


_ONLINEPREDICTRESPONSE = _descriptor.Descriptor(
  name='OnlinePredictResponse',
  full_name='mlappliance.OnlinePredictResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='prediction', full_name='mlappliance.OnlinePredictResponse.prediction', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=155,
  serialized_end=198,
)


_TRAININGDATA = _descriptor.Descriptor(
  name='TrainingData',
  full_name='mlappliance.TrainingData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='source', full_name='mlappliance.TrainingData.source', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inlineData', full_name='mlappliance.TrainingData.inlineData', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='s3URL', full_name='mlappliance.TrainingData.s3URL', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=200,
  serialized_end=323,
)


_BATCHTRAINREQUEST = _descriptor.Descriptor(
  name='BatchTrainRequest',
  full_name='mlappliance.BatchTrainRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trainingData', full_name='mlappliance.BatchTrainRequest.trainingData', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=325,
  serialized_end=393,
)


_MODEL_PARAMETERS_PARAMETER = _descriptor.Descriptor(
  name='Parameter',
  full_name='mlappliance.Model.Parameters.Parameter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='mlappliance.Model.Parameters.Parameter.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='mlappliance.Model.Parameters.Parameter.value', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=776,
  serialized_end=816,
)

_MODEL_PARAMETERS = _descriptor.Descriptor(
  name='Parameters',
  full_name='mlappliance.Model.Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hyperParameters', full_name='mlappliance.Model.Parameters.hyperParameters', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_MODEL_PARAMETERS_PARAMETER, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=696,
  serialized_end=816,
)

_MODEL_PERFORMANCESTATISTICS_PERFORMANCE = _descriptor.Descriptor(
  name='Performance',
  full_name='mlappliance.Model.PerformanceStatistics.Performance',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='metric', full_name='mlappliance.Model.PerformanceStatistics.Performance.metric', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='score', full_name='mlappliance.Model.PerformanceStatistics.Performance.score', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=984,
  serialized_end=1077,
)

_MODEL_PERFORMANCESTATISTICS_ROCPOINT = _descriptor.Descriptor(
  name='ROCPoint',
  full_name='mlappliance.Model.PerformanceStatistics.ROCPoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='falsePositiveRate', full_name='mlappliance.Model.PerformanceStatistics.ROCPoint.falsePositiveRate', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='truePositiveRate', full_name='mlappliance.Model.PerformanceStatistics.ROCPoint.truePositiveRate', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1079,
  serialized_end=1142,
)

_MODEL_PERFORMANCESTATISTICS = _descriptor.Descriptor(
  name='PerformanceStatistics',
  full_name='mlappliance.Model.PerformanceStatistics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='metrics', full_name='mlappliance.Model.PerformanceStatistics.metrics', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rocCurve', full_name='mlappliance.Model.PerformanceStatistics.rocCurve', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_MODEL_PERFORMANCESTATISTICS_PERFORMANCE, _MODEL_PERFORMANCESTATISTICS_ROCPOINT, ],
  enum_types=[
    _MODEL_PERFORMANCESTATISTICS_METRIC,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=819,
  serialized_end=1251,
)

_MODEL_FEATUREIMPORTANCES_FEATUREIMPORTANCE = _descriptor.Descriptor(
  name='FeatureImportance',
  full_name='mlappliance.Model.FeatureImportances.FeatureImportance',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='feature', full_name='mlappliance.Model.FeatureImportances.FeatureImportance.feature', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='importance', full_name='mlappliance.Model.FeatureImportances.FeatureImportance.importance', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1354,
  serialized_end=1410,
)

_MODEL_FEATUREIMPORTANCES = _descriptor.Descriptor(
  name='FeatureImportances',
  full_name='mlappliance.Model.FeatureImportances',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='importances', full_name='mlappliance.Model.FeatureImportances.importances', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_MODEL_FEATUREIMPORTANCES_FEATUREIMPORTANCE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1254,
  serialized_end=1410,
)

_MODEL_SERIALIZED = _descriptor.Descriptor(
  name='Serialized',
  full_name='mlappliance.Model.Serialized',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pickledString', full_name='mlappliance.Model.Serialized.pickledString', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='jsonString', full_name='mlappliance.Model.Serialized.jsonString', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1412,
  serialized_end=1467,
)

_MODEL = _descriptor.Descriptor(
  name='Model',
  full_name='mlappliance.Model',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='algorithm', full_name='mlappliance.Model.algorithm', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parameters', full_name='mlappliance.Model.parameters', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='performanceStatistics', full_name='mlappliance.Model.performanceStatistics', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='featureImportances', full_name='mlappliance.Model.featureImportances', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='serialized', full_name='mlappliance.Model.serialized', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_MODEL_PARAMETERS, _MODEL_PERFORMANCESTATISTICS, _MODEL_FEATUREIMPORTANCES, _MODEL_SERIALIZED, ],
  enum_types=[
    _MODEL_ALGORITHM,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=396,
  serialized_end=1582,
)


_TRAININGREPORT_SUMMARYSTATISTICS = _descriptor.Descriptor(
  name='SummaryStatistics',
  full_name='mlappliance.TrainingReport.SummaryStatistics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='numExamples', full_name='mlappliance.TrainingReport.SummaryStatistics.numExamples', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='numPositives', full_name='mlappliance.TrainingReport.SummaryStatistics.numPositives', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1713,
  serialized_end=1775,
)

_TRAININGREPORT = _descriptor.Descriptor(
  name='TrainingReport',
  full_name='mlappliance.TrainingReport',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='summaryStatistics', full_name='mlappliance.TrainingReport.summaryStatistics', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='models', full_name='mlappliance.TrainingReport.models', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_TRAININGREPORT_SUMMARYSTATISTICS, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1585,
  serialized_end=1775,
)

_TRAININGDATA.fields_by_name['source'].enum_type = _DATASOURCE
_TRAININGDATA.fields_by_name['inlineData'].message_type = _ONLINETRAINREQUEST
_BATCHTRAINREQUEST.fields_by_name['trainingData'].message_type = _TRAININGDATA
_MODEL_PARAMETERS_PARAMETER.containing_type = _MODEL_PARAMETERS;
_MODEL_PARAMETERS.fields_by_name['hyperParameters'].message_type = _MODEL_PARAMETERS_PARAMETER
_MODEL_PARAMETERS.containing_type = _MODEL;
_MODEL_PERFORMANCESTATISTICS_PERFORMANCE.fields_by_name['metric'].enum_type = _MODEL_PERFORMANCESTATISTICS_METRIC
_MODEL_PERFORMANCESTATISTICS_PERFORMANCE.containing_type = _MODEL_PERFORMANCESTATISTICS;
_MODEL_PERFORMANCESTATISTICS_ROCPOINT.containing_type = _MODEL_PERFORMANCESTATISTICS;
_MODEL_PERFORMANCESTATISTICS.fields_by_name['metrics'].message_type = _MODEL_PERFORMANCESTATISTICS_PERFORMANCE
_MODEL_PERFORMANCESTATISTICS.fields_by_name['rocCurve'].message_type = _MODEL_PERFORMANCESTATISTICS_ROCPOINT
_MODEL_PERFORMANCESTATISTICS.containing_type = _MODEL;
_MODEL_PERFORMANCESTATISTICS_METRIC.containing_type = _MODEL_PERFORMANCESTATISTICS;
_MODEL_FEATUREIMPORTANCES_FEATUREIMPORTANCE.containing_type = _MODEL_FEATUREIMPORTANCES;
_MODEL_FEATUREIMPORTANCES.fields_by_name['importances'].message_type = _MODEL_FEATUREIMPORTANCES_FEATUREIMPORTANCE
_MODEL_FEATUREIMPORTANCES.containing_type = _MODEL;
_MODEL_SERIALIZED.containing_type = _MODEL;
_MODEL.fields_by_name['algorithm'].enum_type = _MODEL_ALGORITHM
_MODEL.fields_by_name['parameters'].message_type = _MODEL_PARAMETERS
_MODEL.fields_by_name['performanceStatistics'].message_type = _MODEL_PERFORMANCESTATISTICS
_MODEL.fields_by_name['featureImportances'].message_type = _MODEL_FEATUREIMPORTANCES
_MODEL.fields_by_name['serialized'].message_type = _MODEL_SERIALIZED
_MODEL_ALGORITHM.containing_type = _MODEL;
_TRAININGREPORT_SUMMARYSTATISTICS.containing_type = _TRAININGREPORT;
_TRAININGREPORT.fields_by_name['summaryStatistics'].message_type = _TRAININGREPORT_SUMMARYSTATISTICS
_TRAININGREPORT.fields_by_name['models'].message_type = _MODEL
DESCRIPTOR.message_types_by_name['OnlineTrainRequest'] = _ONLINETRAINREQUEST
DESCRIPTOR.message_types_by_name['OnlineTrainResponse'] = _ONLINETRAINRESPONSE
DESCRIPTOR.message_types_by_name['OnlinePredictRequest'] = _ONLINEPREDICTREQUEST
DESCRIPTOR.message_types_by_name['OnlinePredictResponse'] = _ONLINEPREDICTRESPONSE
DESCRIPTOR.message_types_by_name['TrainingData'] = _TRAININGDATA
DESCRIPTOR.message_types_by_name['BatchTrainRequest'] = _BATCHTRAINREQUEST
DESCRIPTOR.message_types_by_name['Model'] = _MODEL
DESCRIPTOR.message_types_by_name['TrainingReport'] = _TRAININGREPORT

class OnlineTrainRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ONLINETRAINREQUEST

  # @@protoc_insertion_point(class_scope:mlappliance.OnlineTrainRequest)

class OnlineTrainResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ONLINETRAINRESPONSE

  # @@protoc_insertion_point(class_scope:mlappliance.OnlineTrainResponse)

class OnlinePredictRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ONLINEPREDICTREQUEST

  # @@protoc_insertion_point(class_scope:mlappliance.OnlinePredictRequest)

class OnlinePredictResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ONLINEPREDICTRESPONSE

  # @@protoc_insertion_point(class_scope:mlappliance.OnlinePredictResponse)

class TrainingData(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TRAININGDATA

  # @@protoc_insertion_point(class_scope:mlappliance.TrainingData)

class BatchTrainRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BATCHTRAINREQUEST

  # @@protoc_insertion_point(class_scope:mlappliance.BatchTrainRequest)

class Model(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType

  class Parameters(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType

    class Parameter(_message.Message):
      __metaclass__ = _reflection.GeneratedProtocolMessageType
      DESCRIPTOR = _MODEL_PARAMETERS_PARAMETER

      # @@protoc_insertion_point(class_scope:mlappliance.Model.Parameters.Parameter)
    DESCRIPTOR = _MODEL_PARAMETERS

    # @@protoc_insertion_point(class_scope:mlappliance.Model.Parameters)

  class PerformanceStatistics(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType

    class Performance(_message.Message):
      __metaclass__ = _reflection.GeneratedProtocolMessageType
      DESCRIPTOR = _MODEL_PERFORMANCESTATISTICS_PERFORMANCE

      # @@protoc_insertion_point(class_scope:mlappliance.Model.PerformanceStatistics.Performance)

    class ROCPoint(_message.Message):
      __metaclass__ = _reflection.GeneratedProtocolMessageType
      DESCRIPTOR = _MODEL_PERFORMANCESTATISTICS_ROCPOINT

      # @@protoc_insertion_point(class_scope:mlappliance.Model.PerformanceStatistics.ROCPoint)
    DESCRIPTOR = _MODEL_PERFORMANCESTATISTICS

    # @@protoc_insertion_point(class_scope:mlappliance.Model.PerformanceStatistics)

  class FeatureImportances(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType

    class FeatureImportance(_message.Message):
      __metaclass__ = _reflection.GeneratedProtocolMessageType
      DESCRIPTOR = _MODEL_FEATUREIMPORTANCES_FEATUREIMPORTANCE

      # @@protoc_insertion_point(class_scope:mlappliance.Model.FeatureImportances.FeatureImportance)
    DESCRIPTOR = _MODEL_FEATUREIMPORTANCES

    # @@protoc_insertion_point(class_scope:mlappliance.Model.FeatureImportances)

  class Serialized(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _MODEL_SERIALIZED

    # @@protoc_insertion_point(class_scope:mlappliance.Model.Serialized)
  DESCRIPTOR = _MODEL

  # @@protoc_insertion_point(class_scope:mlappliance.Model)

class TrainingReport(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType

  class SummaryStatistics(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _TRAININGREPORT_SUMMARYSTATISTICS

    # @@protoc_insertion_point(class_scope:mlappliance.TrainingReport.SummaryStatistics)
  DESCRIPTOR = _TRAININGREPORT

  # @@protoc_insertion_point(class_scope:mlappliance.TrainingReport)


# @@protoc_insertion_point(module_scope)
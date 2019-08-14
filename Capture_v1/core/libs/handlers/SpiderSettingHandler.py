import inspect


class PythonToMap(object):

    @staticmethod
    def genMap(targetPy):
        targetObj = {}
        for key, obj in inspect.getmembers(targetPy):
            # print("{}:{}".format(key, obj))
            if inspect.isclass(obj):
                continue
            if inspect.ismodule(obj):
                continue
            if '__' in key:
                continue
            if inspect.ismethod(key):
                continue
            targetObj[key] = obj
        # print(targetObj.keys())
        return targetObj



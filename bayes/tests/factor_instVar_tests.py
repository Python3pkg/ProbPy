from bayes.prob.bn import *
from nose.tools import with_setup, nottest

from bayes.tests.factor_base import FactorBase

class TestFactorInstVar(FactorBase):
    def instVar_test_0(self):
        """
        f(X=v)
        """

        res_T = self.X_factor.instVar(self.X.name, "T")
        res_F = self.X_factor.instVar(self.X.name, "F")

        assert(res_T.rand_vars == [] and \
                res_T.values == [1])
        assert(res_F.rand_vars == [] and \
                res_F.values == [2])

    def instVar_test_1(self):
        """
        f(X=v, Y)
        """

        res_T = self.XY_factor.instVar(self.X.name, "T")
        res_F = self.XY_factor.instVar(self.X.name, "F")

        assert(res_T.rand_vars == [self.Y] and \
                res_T.values == [1, 3])
        assert(res_F.rand_vars == [self.Y] and \
                res_F.values == [2, 4])

    def instVar_test_2(self):
        """
        f(X,   Y=v)
        """

        res_T = self.XY_factor.instVar(self.Y.name, "T")
        res_F = self.XY_factor.instVar(self.Y.name, "F")

        assert(res_T.rand_vars == [self.X] and \
                res_T.values == [1, 2])
        assert(res_F.rand_vars == [self.X] and \
                res_F.values == [3, 4])

    def instVar_test_3(self):
        """
        f(X=v, Y=v)
        """

        res_TT = self.XY_factor.instVar(\
                [self.X.name, self.Y.name], ["T", "T"])
        res_FT = self.XY_factor.instVar(\
                [self.X.name, self.Y.name], ["F", "T"])
        res_TF = self.XY_factor.instVar(\
                [self.X.name, self.Y.name], ["T", "F"])
        res_FF = self.XY_factor.instVar(\
                [self.X.name, self.Y.name], ["F", "F"])

        assert(res_TT.rand_vars == [] and res_TT.values == [1])
        assert(res_FT.rand_vars == [] and res_FT.values == [2])
        assert(res_TF.rand_vars == [] and res_TF.values == [3])
        assert(res_FF.rand_vars == [] and res_FF.values == [4])

    def instVar_test_4(self):
        """
        f(X=v, Y,   Z)
        """

        res_T = self.XYZ_factor.instVar(\
                [self.X.name], ["T"])
        res_F = self.XYZ_factor.instVar(\
                [self.X.name], ["F"])

        assert(res_T.rand_vars == [self.Y, self.Z] and \
                res_T.values == [1, 3, 5, 7])
        assert(res_F.rand_vars == [self.Y, self.Z] and \
                res_F.values == [2, 4, 6, 8])

    def instVar_test_5(self):
        """
        f(X,   Y=v, Z)
        """

        res_T = self.XYZ_factor.instVar(\
                [self.Y.name], ["T"])
        res_F = self.XYZ_factor.instVar(\
                [self.Y.name], ["F"])

        assert(res_T.rand_vars == [self.X, self.Z] and \
                res_T.values == [1, 2, 5, 6])
        assert(res_F.rand_vars == [self.X, self.Z] and \
                res_F.values == [3, 4, 7, 8])

    def instVar_test_6(self):
        """
        f(X,   Y,   Z=v)
        """

        res_T = self.XYZ_factor.instVar(\
                [self.Z.name], ["T"])
        res_F = self.XYZ_factor.instVar(\
                [self.Z.name], ["F"])

        assert(res_T.rand_vars == [self.X, self.Y] and \
                res_T.values == [1, 2, 3, 4])
        assert(res_F.rand_vars == [self.X, self.Y] and \
                res_F.values == [5, 6, 7, 8])

    def instVar_test_7(self):
        """
        f(X=v, Y=v, Z)
        """

        res_TT = self.XYZ_factor.instVar(\
                [self.X.name, self.Y.name], ["T", "T"])
        res_TF = self.XYZ_factor.instVar(\
                [self.X.name, self.Y.name], ["T", "F"])
        res_FT = self.XYZ_factor.instVar(\
                [self.X.name, self.Y.name], ["F", "T"])
        res_FF = self.XYZ_factor.instVar(\
                [self.X.name, self.Y.name], ["F", "F"])

        assert(res_TT.rand_vars == [self.Z] and \
               res_TT.values == [1, 5])
        assert(res_TF.rand_vars == [self.Z] and \
               res_TF.values == [3, 7])
        assert(res_FT.rand_vars == [self.Z] and \
               res_FT.values == [2, 6])
        assert(res_FF.rand_vars == [self.Z] and \
               res_FF.values == [4, 8])


    def instVar_test_8(self):
        """
        f(X=v, Y,   Z=v)
        """

        res_TT = self.XYZ_factor.instVar(\
                [self.X.name, self.Z.name], ["T", "T"])
        res_TF = self.XYZ_factor.instVar(\
                [self.X.name, self.Z.name], ["T", "F"])
        res_FT = self.XYZ_factor.instVar(\
                [self.X.name, self.Z.name], ["F", "T"])
        res_FF = self.XYZ_factor.instVar(\
                [self.X.name, self.Z.name], ["F", "F"])

        assert(res_TT.rand_vars == [self.Y] and \
               res_TT.values == [1, 3])
        assert(res_TF.rand_vars == [self.Y] and \
               res_TF.values == [5, 7])
        assert(res_FT.rand_vars == [self.Y] and \
               res_FT.values == [2, 4])
        assert(res_FF.rand_vars == [self.Y] and \
               res_FF.values == [6, 8])

    def instVar_test_9(self):
        """
        f(X,   Y=v, Z=v)
        """

        res_TT = self.XYZ_factor.instVar(\
                [self.Y.name, self.Z.name], ["T", "T"])
        res_TF = self.XYZ_factor.instVar(\
                [self.Y.name, self.Z.name], ["T", "F"])
        res_FT = self.XYZ_factor.instVar(\
                [self.Y.name, self.Z.name], ["F", "T"])
        res_FF = self.XYZ_factor.instVar(\
                [self.Y.name, self.Z.name], ["F", "F"])

        assert(res_TT.rand_vars == [self.X] and \
               res_TT.values == [1, 2])
        assert(res_TF.rand_vars == [self.X] and \
               res_TF.values == [5, 6])
        assert(res_FT.rand_vars == [self.X] and \
               res_FT.values == [3, 4])
        assert(res_FF.rand_vars == [self.X] and \
               res_FF.values == [7, 8])

    def instVar_test_10(self):
        """
        f(X=v, Y=v,   Z=v)
        """

        res_TTT = self.XYZ_factor.instVar(\
                 [self.X.name, self.Y.name, self.Z.name], \
                 ["T", "T", "T"])
        res_FTT = self.XYZ_factor.instVar(\
                 [self.X.name, self.Y.name, self.Z.name], \
                 ["F", "T", "T"])
        res_TFT = self.XYZ_factor.instVar(\
                 [self.X.name, self.Y.name, self.Z.name], \
                 ["T", "F", "T"])
        res_FFT = self.XYZ_factor.instVar(\
                 [self.X.name, self.Y.name, self.Z.name], \
                 ["F", "F", "T"])
        res_TTF = self.XYZ_factor.instVar(\
                 [self.X.name, self.Y.name, self.Z.name], \
                 ["T", "T", "F"])
        res_FTF = self.XYZ_factor.instVar(\
                 [self.X.name, self.Y.name, self.Z.name], \
                 ["F", "T", "F"])
        res_TFF = self.XYZ_factor.instVar(\
                 [self.X.name, self.Y.name, self.Z.name], \
                 ["T", "F", "F"])
        res_FFF = self.XYZ_factor.instVar(\
                 [self.X.name, self.Y.name, self.Z.name], \
                 ["F", "F", "F"])

        assert(res_TTT.rand_vars == [] and res_TTT.values == [1])
        assert(res_FTT.rand_vars == [] and res_FTT.values == [2])
        assert(res_TFT.rand_vars == [] and res_TFT.values == [3])
        assert(res_FFT.rand_vars == [] and res_FFT.values == [4])
        assert(res_TTF.rand_vars == [] and res_TTF.values == [5])
        assert(res_FTF.rand_vars == [] and res_FTF.values == [6])
        assert(res_TFF.rand_vars == [] and res_TFF.values == [7])
        assert(res_FFF.rand_vars == [] and res_FFF.values == [8])


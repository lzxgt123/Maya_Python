# .-*- coding: utf-8 -*-
# .FileName:correctiveBS_Tool
# .Date....:2022-03-21 : 11 :10
# .Author..:Qian binjie
# .Contact.:1075064966@qq.com
'''
launch :
        import correctiveBS_Tool as QBJ_correctiveBS_Tool
        reload(QBJ_correctiveBS_Tool)
'''

import maya.cmds as cmds
import maya.OpenMaya as om


class CorrectiveBsTool(object):

    def __init__(self):
        pass


    def mesh_judge(self,object):
        '''
        :param object: 需要被判断的对象
        :return: 是否为mesh对象
        '''
        cmds.select(object,r=True)
        cmds.pickWalk(direction='down')
        child = cmds.ls(sl=1)
        cmds.select(cl=True)
        if cmds.nodeType(child) == 'mesh':
            return True
        else:
            return None


    def load_BaseGeo(self):
        u'''

        :return: 返回选择的polygon 名称
        '''
        baseGeo = cmds.ls(sl=True)
        if len(baseGeo) == 1:
            if self.mesh_judge(baseGeo):
                return baseGeo[0]
            else:
                om.MGlobal_displayWarning('QBJ_Tip : Please select "polygon" ! ')
        else:
            om.MGlobal_displayError('QBJ_Tip : Please select only one object !!! ')


    def load_targetGeo(self,baseGeo):
        if baseGeo:
            targetGeo = baseGeo + '_target'
            if cmds.ls(targetGeo):
                return targetGeo
            else:
                targetGeo = cmds.ls(sl=True)
                if len(targetGeo) == 1:
                    if self.mesh_judge(targetGeo):
                        return targetGeo[0]
                else:
                    om.MGlobal_displayError('QBJ_Tip : Please select only one object !!! ')


    def get_blendshape(self,baseGeo):
        if baseGeo:
            baseGeo_history = cmds.listHistory(baseGeo,pruneDagObjects=True)
            bs_node = cmds.ls(baseGeo_history,type='blendShape')
            if bs_node :
                return bs_node
            else:
                return None


    def add_blendShape(self,targetGeo,baseGeo):
        # 给baseGeo添加blendShape
        if targetGeo and baseGeo:
            blendShapeNode = cmds.blendShape(targetGeo,baseGeo,name='{}_bs'.format(baseGeo),frontOfChain=True,tc=True)

            return blendShapeNode


    def del_blendShape(self,bs_node):
       if bs_node:
           cmds.delete(bs_node)


    def connect_to_poseGrp(self):
        pass

    def create_armTargets(self,targetGeo):
        pass

    def create_legTargets(self,targetGeo):
        pass

    def create_fingerTargets(self,targetGeo):
        pass

    def create_torsoTargets(self,targetGeo):
        pass
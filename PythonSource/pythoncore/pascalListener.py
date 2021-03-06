# Generated from pascal.g4 by ANTLR 4.5.3
import pascalLoveParser
from PascalBuildHandler import PascalBuildHandler
from antlr4 import *
from pascalUseHandler import pascalUseHandler

if __name__ is not None and "." in __name__:
    from .pascalParser import pascalParser
else:
    from pascalParser import pascalParser

"""
#This class defines a complete listener for a parse tree
#produced by pascalParser.
 """


class pascalListener(ParseTreeListener):
    _PARSER = pascalLoveParser
    _BUILD = PascalBuildHandler
    _USEHANDLER = pascalUseHandler
    _CURRENTFLAG = 0
    _PARAMETERS = []
    _LASTSTRUCTURE = None

    '''
    Flags
    0 - no state
    1 - program head - next var is a program name
    2 - program head Parameters - next var is a series of parameters
    3 - use statement - next var is a series of import names to find locally or externally
    4 - Function is currently being processed.
    5 - Entered parameter section
    6 - Function / procedure name write
    7 - Variable declaration entered
    8 - Current entered variable
    9 - Enter a expression structure
    10-Constant variable flag
    11-Unalabelled statement's
    12- everything flagged in 12 is placed into main method
    '''

    # init function to set all prelimenary variables
    def __init__(self, ParseTreeListener, filename):
        self._PARSER = pascalLoveParser
        self._BUILD = PascalBuildHandler
        self._USEHANDLER = pascalUseHandler
        self._CURRENTFLAG = 0
        self._PARAMETERS = []
        self._LASTSTRUCTURE = None

    # Enter a parse tree produced by pascalParser#program.
    def enterProgram(self, ctx: pascalParser.ProgramContext):
        pass

    # Exit a parse tree produced by pascalParser#program.
    def exitProgram(self, ctx: pascalParser.ProgramContext):
        #self._BUILD._write_function_end(self._BUILD)
        pass

    # Enter a parse tree produced by pascalParser#programHeading.
    def enterProgramHeading(self, ctx: pascalParser.ProgramHeadingContext):
        self._CURRENTFLAG = 1
        #print((ctx.getText()))
        pass

    # Exit a parse tree produced by pascalParser#programHeading.
    def exitProgramHeading(self, ctx: pascalParser.ProgramHeadingContext):
        self._CURRENTFLAG = 0
        #self._BUILD._write_function(self._BUILD, ctx.getText())
        # self._BUILD._build_file(self)
        pass

    # Enter a parse tree produced by pascalParser#identifier.
    def enterIdentifier(self, ctx: pascalParser.IdentifierContext):
        if self._CURRENTFLAG == 1:
            self._CURRENTFLAG = 2
            self._BUILD._create_output_dir(self._BUILD, ctx.getText())
            self._BUILD._create_file(self._BUILD, ctx.getText())
        elif self._CURRENTFLAG == 2:
            # print((ctx.getText()))
            pass
        elif self._CURRENTFLAG == 3:
            self._USEHANDLER.find_module(self, ctx.getText())
        elif (self._CURRENTFLAG == 4):
            self._BUILD._write_function(self._BUILD, ctx.getText())
            self._CURRENTFLAG = 0
            pass
        elif self._CURRENTFLAG == 5:
            self._PARAMETERS.append(ctx.getText())
        elif self._CURRENTFLAG == 6:
            self._BUILD._write_function(self._BUILD, ctx.getText())
            self._CURRENTFLAG = 0
        elif self._CURRENTFLAG == 7:
            self._BUILD._write_(self._BUILD, ctx.getText())
            self._CURRENTFLAG = 0
        elif self._CURRENTFLAG == 10:
            # self._BUILD._write_(self._BUILD, ctx.getText())
            self._CURRENTFLAG = 0

        else:
            self._BUILD._write_(self._BUILD, ctx.getText())
        pass

    # Exit a parse tree produced by pascalParser#identifier.
    def exitIdentifier(self, ctx: pascalParser.IdentifierContext):
        pass

    # Enter a parse tree produced by pascalParser#block.
    def enterBlock(self, ctx: pascalParser.BlockContext):
        self._BUILD._write_enterBlock(self._BUILD)
        pass

    # Exit a parse tree produced by pascalParser#block.
    def exitBlock(self, ctx: pascalParser.BlockContext):
        self._BUILD._write_exitBlock(self._BUILD)
        self._CURRENTFLAG = 0
        pass

    # Enter a parse tree produced by pascalParser#usesUnitsPart.
    def enterUsesUnitsPart(self, ctx: pascalParser.UsesUnitsPartContext):
        self._CURRENTFLAG = 2
        self._BUILD._test_uses(self._BUILD, ctx.getText())
        pass

    # Exit a parse tree produced by pascalParser#usesUnitsPart.
    def exitUsesUnitsPart(self, ctx: pascalParser.UsesUnitsPartContext):
        self._CURRENTFLAG = 0
        pass

    # Enter a parse tree produced by pascalParser#labelDeclarationPart.
    def enterLabelDeclarationPart(self, ctx: pascalParser.LabelDeclarationPartContext):
        pass

    # Exit a parse tree produced by pascalParser#labelDeclarationPart.
    def exitLabelDeclarationPart(self, ctx: pascalParser.LabelDeclarationPartContext):
        pass

    # Enter a parse tree produced by pascalParser#label.
    def enterLabel(self, ctx: pascalParser.LabelContext):
        pass

    # Exit a parse tree produced by pascalParser#label.
    def exitLabel(self, ctx: pascalParser.LabelContext):
        pass

    # Enter a parse tree produced by pascalParser#constantDefinitionPart.
    def enterConstantDefinitionPart(self, ctx: pascalParser.ConstantDefinitionPartContext):
        pass

    # Exit a parse tree produced by pascalParser#constantDefinitionPart.
    def exitConstantDefinitionPart(self, ctx: pascalParser.ConstantDefinitionPartContext):
        pass

    # Enter a parse tree produced by pascalParser#constantDefinition.
    def enterConstantDefinition(self, ctx: pascalParser.ConstantDefinitionContext):
        self._CURRENTFLAG = 10
        self._BUILD._write_constant(self._BUILD, ctx)
        #print(ctx.getChild(0).getText())
        pass

    # Exit a parse tree produced by pascalParser#constantDefinition.
    def exitConstantDefinition(self, ctx: pascalParser.ConstantDefinitionContext):
        self._CURRENTFLAG = 0
        self._BUILD._write_constant_exit(self._BUILD)
        pass

    # Enter a parse tree produced by pascalParser#constantChr.
    def enterConstantChr(self, ctx: pascalParser.ConstantChrContext):
        pass

    # Exit a parse tree produced by pascalParser#constantChr.
    def exitConstantChr(self, ctx: pascalParser.ConstantChrContext):
        pass

    # Enter a parse tree produced by pascalParser#constant.
    def enterConstant(self, ctx: pascalParser.ConstantContext):
        pass

    # Exit a parse tree produced by pascalParser#constant.
    def exitConstant(self, ctx: pascalParser.ConstantContext):
        pass

    # Enter a parse tree produced by pascalParser#unsignedNumber.
    def enterUnsignedNumber(self, ctx: pascalParser.UnsignedNumberContext):
        pass

    # Exit a parse tree produced by pascalParser#unsignedNumber.
    def exitUnsignedNumber(self, ctx: pascalParser.UnsignedNumberContext):
        pass

    # Enter a parse tree produced by pascalParser#unsignedInteger.
    def enterUnsignedInteger(self, ctx: pascalParser.UnsignedIntegerContext):
        self._BUILD._write_int(self._BUILD,ctx.getText())
        pass

    # Exit a parse tree produced by pascalParser#unsignedInteger.
    def exitUnsignedInteger(self, ctx: pascalParser.UnsignedIntegerContext):
        pass

    # Enter a parse tree produced by pascalParser#unsignedReal.
    def enterUnsignedReal(self, ctx: pascalParser.UnsignedRealContext):
        pass

    # Exit a parse tree produced by pascalParser#unsignedReal.
    def exitUnsignedReal(self, ctx: pascalParser.UnsignedRealContext):
        pass

    # Enter a parse tree produced by pascalParser#sign.
    def enterSign(self, ctx: pascalParser.SignContext):
        pass

    # Exit a parse tree produced by pascalParser#sign.
    def exitSign(self, ctx: pascalParser.SignContext):
        pass

    # Enter a parse tree produced by pascalParser#string.
    def enterString(self, ctx: pascalParser.StringContext):
        pass

    # Exit a parse tree produced by pascalParser#string.
    def exitString(self, ctx: pascalParser.StringContext):
        pass

    # Enter a parse tree produced by pascalParser#typeDefinitionPart.
    def enterTypeDefinitionPart(self, ctx: pascalParser.TypeDefinitionPartContext):
        self._BUILD._write_type_declaration_part(self._BUILD)
        pass

    # Exit a parse tree produced by pascalParser#typeDefinitionPart.
    def exitTypeDefinitionPart(self, ctx: pascalParser.TypeDefinitionPartContext):
        pass

    # Enter a parse tree produced by pascalParser#typeDefinition.
    def enterTypeDefinition(self, ctx: pascalParser.TypeDefinitionContext):
        pass

    # Exit a parse tree produced by pascalParser#typeDefinition.
    def exitTypeDefinition(self, ctx: pascalParser.TypeDefinitionContext):
        pass

    # Enter a parse tree produced by pascalParser#functionType.
    def enterFunctionType(self, ctx: pascalParser.FunctionTypeContext):
        pass

    # Exit a parse tree produced by pascalParser#functionType.
    def exitFunctionType(self, ctx: pascalParser.FunctionTypeContext):
        pass

    # Enter a parse tree produced by pascalParser#procedureType.
    def enterProcedureType(self, ctx: pascalParser.ProcedureTypeContext):
        pass

    # Exit a parse tree produced by pascalParser#procedureType.
    def exitProcedureType(self, ctx: pascalParser.ProcedureTypeContext):
        pass

    # Enter a parse tree produced by pascalParser#typeT.
    def enterTypeT(self, ctx: pascalParser.TypeTContext):
        pass

    # Exit a parse tree produced by pascalParser#typeT.
    def exitTypeT(self, ctx: pascalParser.TypeTContext):
        pass

    # Enter a parse tree produced by pascalParser#simpleType.
    def enterSimpleType(self, ctx: pascalParser.SimpleTypeContext):
        pass

    # Exit a parse tree produced by pascalParser#simpleType.
    def exitSimpleType(self, ctx: pascalParser.SimpleTypeContext):
        pass

    # Enter a parse tree produced by pascalParser#scalarType.
    def enterScalarType(self, ctx: pascalParser.ScalarTypeContext):
        pass

    # Exit a parse tree produced by pascalParser#scalarType.
    def exitScalarType(self, ctx: pascalParser.ScalarTypeContext):
        pass

    # Enter a parse tree produced by pascalParser#subrangeType.
    def enterSubrangeType(self, ctx: pascalParser.SubrangeTypeContext):
        pass

    # Exit a parse tree produced by pascalParser#subrangeType.
    def exitSubrangeType(self, ctx: pascalParser.SubrangeTypeContext):
        pass

    # Enter a parse tree produced by pascalParser#typeIdentifier.
    def enterTypeIdentifier(self, ctx: pascalParser.TypeIdentifierContext):
        pass

    # Exit a parse tree produced by pascalParser#typeIdentifier.
    def exitTypeIdentifier(self, ctx: pascalParser.TypeIdentifierContext):
        pass

    # Enter a parse tree produced by pascalParser#structuredType.
    def enterStructuredType(self, ctx: pascalParser.StructuredTypeContext):
        pass

    # Exit a parse tree produced by pascalParser#structuredType.
    def exitStructuredType(self, ctx: pascalParser.StructuredTypeContext):
        pass

    # Enter a parse tree produced by pascalParser#unpackedStructuredType.
    def enterUnpackedStructuredType(self, ctx: pascalParser.UnpackedStructuredTypeContext):
        pass

    # Exit a parse tree produced by pascalParser#unpackedStructuredType.
    def exitUnpackedStructuredType(self, ctx: pascalParser.UnpackedStructuredTypeContext):
        pass

    # Enter a parse tree produced by pascalParser#stringtype.
    def enterStringtype(self, ctx: pascalParser.StringtypeContext):
        pass

    # Exit a parse tree produced by pascalParser#stringtype.
    def exitStringtype(self, ctx: pascalParser.StringtypeContext):
        pass

    # Enter a parse tree produced by pascalParser#arrayType.
    def enterArrayType(self, ctx: pascalParser.ArrayTypeContext):
        pass

    # Exit a parse tree produced by pascalParser#arrayType.
    def exitArrayType(self, ctx: pascalParser.ArrayTypeContext):
        pass

    # Enter a parse tree produced by pascalParser#typeList.
    def enterTypeList(self, ctx: pascalParser.TypeListContext):
        pass

    # Exit a parse tree produced by pascalParser#typeList.
    def exitTypeList(self, ctx: pascalParser.TypeListContext):
        pass

    # Enter a parse tree produced by pascalParser#indexType.
    def enterIndexType(self, ctx: pascalParser.IndexTypeContext):
        pass

    # Exit a parse tree produced by pascalParser#indexType.
    def exitIndexType(self, ctx: pascalParser.IndexTypeContext):
        pass

    # Enter a parse tree produced by pascalParser#componentType.
    def enterComponentType(self, ctx: pascalParser.ComponentTypeContext):
        pass

    # Exit a parse tree produced by pascalParser#componentType.
    def exitComponentType(self, ctx: pascalParser.ComponentTypeContext):
        pass

    # Enter a parse tree produced by pascalParser#recordType.
    def enterRecordType(self, ctx: pascalParser.RecordTypeContext):
        pass

    # Exit a parse tree produced by pascalParser#recordType.
    def exitRecordType(self, ctx: pascalParser.RecordTypeContext):
        pass

    # Enter a parse tree produced by pascalParser#fieldList.
    def enterFieldList(self, ctx: pascalParser.FieldListContext):
        pass

    # Exit a parse tree produced by pascalParser#fieldList.
    def exitFieldList(self, ctx: pascalParser.FieldListContext):
        pass

    # Enter a parse tree produced by pascalParser#fixedPart.
    def enterFixedPart(self, ctx: pascalParser.FixedPartContext):
        pass

    # Exit a parse tree produced by pascalParser#fixedPart.
    def exitFixedPart(self, ctx: pascalParser.FixedPartContext):
        pass

    # Enter a parse tree produced by pascalParser#recordSection.
    def enterRecordSection(self, ctx: pascalParser.RecordSectionContext):
        pass

    # Exit a parse tree produced by pascalParser#recordSection.
    def exitRecordSection(self, ctx: pascalParser.RecordSectionContext):
        pass

    # Enter a parse tree produced by pascalParser#variantPart.
    def enterVariantPart(self, ctx: pascalParser.VariantPartContext):
        pass

    # Exit a parse tree produced by pascalParser#variantPart.
    def exitVariantPart(self, ctx: pascalParser.VariantPartContext):
        pass

    # Enter a parse tree produced by pascalParser#tag.
    def enterTag(self, ctx: pascalParser.TagContext):
        pass

    # Exit a parse tree produced by pascalParser#tag.
    def exitTag(self, ctx: pascalParser.TagContext):
        pass

    # Enter a parse tree produced by pascalParser#variant.
    def enterVariant(self, ctx: pascalParser.VariantContext):
        pass

    # Exit a parse tree produced by pascalParser#variant.
    def exitVariant(self, ctx: pascalParser.VariantContext):
        pass

    # Enter a parse tree produced by pascalParser#setType.
    def enterSetType(self, ctx: pascalParser.SetTypeContext):
        pass

    # Exit a parse tree produced by pascalParser#setType.
    def exitSetType(self, ctx: pascalParser.SetTypeContext):
        pass

    # Enter a parse tree produced by pascalParser#baseType.
    def enterBaseType(self, ctx: pascalParser.BaseTypeContext):
        pass

    # Exit a parse tree produced by pascalParser#baseType.
    def exitBaseType(self, ctx: pascalParser.BaseTypeContext):
        pass

    # Enter a parse tree produced by pascalParser#fileType.
    def enterFileType(self, ctx: pascalParser.FileTypeContext):
        pass

    # Exit a parse tree produced by pascalParser#fileType.
    def exitFileType(self, ctx: pascalParser.FileTypeContext):
        pass

    # Enter a parse tree produced by pascalParser#pointerType.
    def enterPointerType(self, ctx: pascalParser.PointerTypeContext):
        pass

    # Exit a parse tree produced by pascalParser#pointerType.
    def exitPointerType(self, ctx: pascalParser.PointerTypeContext):
        pass

    # Enter a parse tree produced by pascalParser#variableDeclarationPart.
    def enterVariableDeclarationPart(self, ctx: pascalParser.VariableDeclarationPartContext):
        pass

    # Exit a parse tree produced by pascalParser#variableDeclarationPart.
    def exitVariableDeclarationPart(self, ctx: pascalParser.VariableDeclarationPartContext):
        pass

    # Enter a parse tree produced by pascalParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx: pascalParser.VariableDeclarationContext):
        self._BUILD._write_variable(self._BUILD)
        self._CURRENTFLAG = 7
        if self._LASTSTRUCTURE is 0:
            self._BUILD._write_variable_declaration(self._BUILD, True)
        else:
            self._BUILD._write_variable_declaration(self._BUILD, False)
        pass

    # Exit a parse tree produced by pascalParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx: pascalParser.VariableDeclarationContext):
        self._CURRENTFLAG = 0
        pass

    # Enter a parse tree produced by pascalParser#procedureAndFunctionDeclarationPart.
    def enterProcedureAndFunctionDeclarationPart(self, ctx: pascalParser.ProcedureAndFunctionDeclarationPartContext):
        pass

    # Exit a parse tree produced by pascalParser#procedureAndFunctionDeclarationPart.
    def exitProcedureAndFunctionDeclarationPart(self, ctx: pascalParser.ProcedureAndFunctionDeclarationPartContext):
        pass

    # Enter a parse tree produced by pascalParser#procedureOrFunctionDeclaration.
    def enterProcedureOrFunctionDeclaration(self, ctx: pascalParser.ProcedureOrFunctionDeclarationContext):
        pass

    # Exit a parse tree produced by pascalParser#procedureOrFunctionDeclaration.
    def exitProcedureOrFunctionDeclaration(self, ctx: pascalParser.ProcedureOrFunctionDeclarationContext):
        pass

    # Enter a parse tree produced by pascalParser#procedureDeclaration.
    def enterProcedureDeclaration(self, ctx: pascalParser.ProcedureDeclarationContext):
        self._CURRENTFLAG = 6  # set that a function is being processed
        self._LASTSTRUCTURE = 6  # set last used for recording purposes
        pass

    # Exit a parse tree produced by pascalParser#procedureDeclaration.
    def exitProcedureDeclaration(self, ctx: pascalParser.ProcedureDeclarationContext):
        self._BUILD._write_function_end(self._BUILD)
        self._LASTSTRUCTURE = 0  # set last used for recording purposes
        self._CURRENTFLAG = 0
        pass

    # Enter a parse tree produced by pascalParser#formalParameterList.
    def enterFormalParameterList(self, ctx: pascalParser.FormalParameterListContext):
        # self._LASTSTRUCTURE = 0 #set last used for recording purposes
        self._BUILD._write_(self._BUILD, "(")  # write out new line to for bodies
        pass

    # Exit a parse tree produced by pascalParser#formalParameterList.
    def exitFormalParameterList(self, ctx: pascalParser.FormalParameterListContext):
        self._BUILD._write_(self._BUILD, ")\n")  # write out new line to for bodies
        pass

    # Enter a parse tree produced by pascalParser#formalParameterSection.
    def enterFormalParameterSection(self, ctx: pascalParser.FormalParameterSectionContext):
        self._CURRENTFLAG = 5

        pass

    # Exit a parse tree produced by pascalParser#formalParameterSection.
    def exitFormalParameterSection(self, ctx: pascalParser.FormalParameterSectionContext):
        self._CURRENTFLAG = self._LASTSTRUCTURE
        # self._BUILD._write_(self._BUILD, "\n")  # write out new line to for bodies
        pass

    # Enter a parse tree produced by pascalParser#parameterGroup.
    def enterParameterGroup(self, ctx: pascalParser.ParameterGroupContext):
        pass

    # Exit a parse tree produced by pascalParser#parameterGroup.
    def exitParameterGroup(self, ctx: pascalParser.ParameterGroupContext):
        pass

    # Enter a parse tree produced by pascalParser#identifierList.
    def enterIdentifierList(self, ctx: pascalParser.IdentifierListContext):
        pass

    # Exit a parse tree produced by pascalParser#identifierList.
    def exitIdentifierList(self, ctx: pascalParser.IdentifierListContext):
        pass

    # Enter a parse tree produced by pascalParser#constList.
    def enterConstList(self, ctx: pascalParser.ConstListContext):
        pass

    # Exit a parse tree produced by pascalParser#constList.
    def exitConstList(self, ctx: pascalParser.ConstListContext):
        pass

    # Enter a parse tree produced by pascalParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx: pascalParser.FunctionDeclarationContext):
        if ctx.formalParameterList is None:
            print('is none')
        self._CURRENTFLAG = 4  # set that a function is being processed
        self._LASTSTRUCTURE = 4  # set last used for recording purposes
        pass

    # Exit a parse tree produced by pascalParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx: pascalParser.FunctionDeclarationContext):
        self._CURRENTFLAG = 0
        # self._BUILD._write_function(self._BUILD,"add")
        del self._PARAMETERS[:]  # empty any stored parameters from function
        # self._BUILD._write_function_end(self._BUILD)
        self._BUILD._write_function_end(self._BUILD)
        pass

    # Enter a parse tree produced by pascalParser#resultType.
    def enterResultType(self, ctx: pascalParser.ResultTypeContext):
        pass

    # Exit a parse tree produced by pascalParser#resultType.
    def exitResultType(self, ctx: pascalParser.ResultTypeContext):
        pass

    # Enter a parse tree produced by pascalParser#statement.
    def enterStatement(self, ctx: pascalParser.StatementContext):
        pass

    # Exit a parse tree produced by pascalParser#statement.
    def exitStatement(self, ctx: pascalParser.StatementContext):
        pass

    # Enter a parse tree produced by pascalParser#unlabelledStatement.
    def enterUnlabelledStatement(self, ctx: pascalParser.UnlabelledStatementContext):
        pass

    # Exit a parse tree produced by pascalParser#unlabelledStatement.
    def exitUnlabelledStatement(self, ctx: pascalParser.UnlabelledStatementContext):
        pass

    # Enter a parse tree produced by pascalParser#simpleStatement.
    def enterSimpleStatement(self, ctx: pascalParser.SimpleStatementContext):
        pass

    # Exit a parse tree produced by pascalParser#simpleStatement.
    def exitSimpleStatement(self, ctx: pascalParser.SimpleStatementContext):
        pass

    # Enter a parse tree produced by pascalParser#assignmentStatement.
    def enterAssignmentStatement(self, ctx: pascalParser.AssignmentStatementContext):
        pass

    # Exit a parse tree produced by pascalParser#assignmentStatement.
    def exitAssignmentStatement(self, ctx: pascalParser.AssignmentStatementContext):
        pass

    # Enter a parse tree produced by pascalParser#variable.
    def enterVariable(self, ctx: pascalParser.VariableContext):
        # implement a variable lookup table here later for type checking
        self._CURRENTFLAG = 8
        self._BUILD._write_(self._BUILD, ctx.getText())
        # replace with a new build method to check table
        pass

    # Exit a parse tree produced by pascalParser#variable.
    def exitVariable(self, ctx: pascalParser.VariableContext):
        self._CURRENTFLAG = 0
        pass

    # Enter a parse tree produced by pascalParser#expression.
    def enterExpression(self, ctx: pascalParser.ExpressionContext):
        self._CURRENTFLAG = 9
        pass

    # Exit a parse tree produced by pascalParser#expression.
    def exitExpression(self, ctx: pascalParser.ExpressionContext):
        pass

    # Enter a parse tree produced by pascalParser#simpleExpression.
    def enterSimpleExpression(self, ctx: pascalParser.SimpleExpressionContext):
        self._BUILD._write_function_expression(self._BUILD,ctx.getText())
        pass

    # Exit a parse tree produced by pascalParser#simpleExpression.
    def exitSimpleExpression(self, ctx: pascalParser.SimpleExpressionContext):
        pass

    # Enter a parse tree produced by pascalParser#term.
    def enterTerm(self, ctx: pascalParser.TermContext):
        pass

    # Exit a parse tree produced by pascalParser#term.
    def exitTerm(self, ctx: pascalParser.TermContext):
        pass

    # Enter a parse tree produced by pascalParser#signedFactor.
    def enterSignedFactor(self, ctx: pascalParser.SignedFactorContext):
        pass

    # Exit a parse tree produced by pascalParser#signedFactor.
    def exitSignedFactor(self, ctx: pascalParser.SignedFactorContext):
        pass

    # Enter a parse tree produced by pascalParser#factor.
    def enterFactor(self, ctx: pascalParser.FactorContext):
        pass

    # Exit a parse tree produced by pascalParser#factor.
    def exitFactor(self, ctx: pascalParser.FactorContext):
        pass

    # Enter a parse tree produced by pascalParser#unsignedConstant.
    def enterUnsignedConstant(self, ctx: pascalParser.UnsignedConstantContext):
        pass

    # Exit a parse tree produced by pascalParser#unsignedConstant.
    def exitUnsignedConstant(self, ctx: pascalParser.UnsignedConstantContext):
        pass

    # Enter a parse tree produced by pascalParser#functionDesignator.
    def enterFunctionDesignator(self, ctx: pascalParser.FunctionDesignatorContext):
        pass

    # Exit a parse tree produced by pascalParser#functionDesignator.
    def exitFunctionDesignator(self, ctx: pascalParser.FunctionDesignatorContext):
        pass

    # Enter a parse tree produced by pascalParser#parameterList.
    def enterParameterList(self, ctx: pascalParser.ParameterListContext):
        pass

    # Exit a parse tree produced by pascalParser#parameterList.
    def exitParameterList(self, ctx: pascalParser.ParameterListContext):
        pass

    # Enter a parse tree produced by pascalParser#setT.
    def enterSetT(self, ctx: pascalParser.SetTContext):
        pass

    # Exit a parse tree produced by pascalParser#setT.
    def exitSetT(self, ctx: pascalParser.SetTContext):
        pass

    # Enter a parse tree produced by pascalParser#elementList.
    def enterElementList(self, ctx: pascalParser.ElementListContext):
        pass

    # Exit a parse tree produced by pascalParser#elementList.
    def exitElementList(self, ctx: pascalParser.ElementListContext):
        pass

    # Enter a parse tree produced by pascalParser#element.
    def enterElement(self, ctx: pascalParser.ElementContext):
        pass

    # Exit a parse tree produced by pascalParser#element.
    def exitElement(self, ctx: pascalParser.ElementContext):
        pass

    # Enter a parse tree produced by pascalParser#procedureStatement.
    def enterProcedureStatement(self, ctx: pascalParser.ProcedureStatementContext):

        pass

    # Exit a parse tree produced by pascalParser#procedureStatement.
    def exitProcedureStatement(self, ctx: pascalParser.ProcedureStatementContext):
        pass

    # Enter a parse tree produced by pascalParser#actualParameter.
    def enterActualParameter(self, ctx: pascalParser.ActualParameterContext):
        pass

    # Exit a parse tree produced by pascalParser#actualParameter.
    def exitActualParameter(self, ctx: pascalParser.ActualParameterContext):
        pass

    # Enter a parse tree produced by pascalParser#gotoStatement.
    def enterGotoStatement(self, ctx: pascalParser.GotoStatementContext):
        pass

    # Exit a parse tree produced by pascalParser#gotoStatement.
    def exitGotoStatement(self, ctx: pascalParser.GotoStatementContext):
        pass

    # Enter a parse tree produced by pascalParser#emptyStatement.
    def enterEmptyStatement(self, ctx: pascalParser.EmptyStatementContext):
        pass

    # Exit a parse tree produced by pascalParser#emptyStatement.
    def exitEmptyStatement(self, ctx: pascalParser.EmptyStatementContext):
        pass

    # Enter a parse tree produced by pascalParser#empty.
    def enterEmpty(self, ctx: pascalParser.EmptyContext):
        pass

    # Exit a parse tree produced by pascalParser#empty.
    def exitEmpty(self, ctx: pascalParser.EmptyContext):
        pass

    # Enter a parse tree produced by pascalParser#structuredStatement.
    def enterStructuredStatement(self, ctx: pascalParser.StructuredStatementContext):
        pass

    # Exit a parse tree produced by pascalParser#structuredStatement.
    def exitStructuredStatement(self, ctx: pascalParser.StructuredStatementContext):
        pass

    # Enter a parse tree produced by pascalParser#compoundStatement.
    def enterCompoundStatement(self, ctx: pascalParser.CompoundStatementContext):
        if self._CURRENTFLAG ==0:
            self._CURRENTFLAG = 11
            self._BUILD._write_compoundStatement(self._BUILD);
        if self._CURRENTFLAG != 4 and self._LASTSTRUCTURE != 6:
            print(ctx.getText())

    pass

    # Exit a parse tree produced by pascalParser#compoundStatement.
    def exitCompoundStatement(self, ctx: pascalParser.CompoundStatementContext):
        self._CURRENTFLAG = 0
        #  self._BUILD._write_function_end(self._BUILD)
        pass

    # Enter a parse tree produced by pascalParser#statements.
    def enterStatements(self, ctx: pascalParser.StatementsContext):
        pass

    # Exit a parse tree produced by pascalParser#statements.
    def exitStatements(self, ctx: pascalParser.StatementsContext):
        pass

    # Enter a parse tree produced by pascalParser#conditionalStatement.
    def enterConditionalStatement(self, ctx: pascalParser.ConditionalStatementContext):
        pass

    # Exit a parse tree produced by pascalParser#conditionalStatement.
    def exitConditionalStatement(self, ctx: pascalParser.ConditionalStatementContext):
        pass

    # Enter a parse tree produced by pascalParser#ifStatement.
    def enterIfStatement(self, ctx: pascalParser.IfStatementContext):
        pass

    # Exit a parse tree produced by pascalParser#ifStatement.
    def exitIfStatement(self, ctx: pascalParser.IfStatementContext):
        pass

    # Enter a parse tree produced by pascalParser#caseStatement.
    def enterCaseStatement(self, ctx: pascalParser.CaseStatementContext):
        pass

    # Exit a parse tree produced by pascalParser#caseStatement.
    def exitCaseStatement(self, ctx: pascalParser.CaseStatementContext):
        pass

    # Enter a parse tree produced by pascalParser#caseListElement.
    def enterCaseListElement(self, ctx: pascalParser.CaseListElementContext):
        pass

    # Exit a parse tree produced by pascalParser#caseListElement.
    def exitCaseListElement(self, ctx: pascalParser.CaseListElementContext):
        pass

    # Enter a parse tree produced by pascalParser#repetetiveStatement.
    def enterRepetetiveStatement(self, ctx: pascalParser.RepetetiveStatementContext):
        pass

    # Exit a parse tree produced by pascalParser#repetetiveStatement.
    def exitRepetetiveStatement(self, ctx: pascalParser.RepetetiveStatementContext):
        pass

    # Enter a parse tree produced by pascalParser#whileStatement.
    def enterWhileStatement(self, ctx: pascalParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by pascalParser#whileStatement.
    def exitWhileStatement(self, ctx: pascalParser.WhileStatementContext):
        pass

    # Enter a parse tree produced by pascalParser#repeatStatement.
    def enterRepeatStatement(self, ctx: pascalParser.RepeatStatementContext):
        pass

    # Exit a parse tree produced by pascalParser#repeatStatement.
    def exitRepeatStatement(self, ctx: pascalParser.RepeatStatementContext):
        pass

    # Enter a parse tree produced by pascalParser#forStatement.
    def enterForStatement(self, ctx: pascalParser.ForStatementContext):
        self._BUILD._write_forLoop(self._BUILD);
        pass

    # Exit a parse tree produced by pascalParser#forStatement.
    def exitForStatement(self, ctx: pascalParser.ForStatementContext):
        self._BUILD._write_function_end(self._BUILD);
        pass

    # Enter a parse tree produced by pascalParser#forList.
    def enterForList(self, ctx: pascalParser.ForListContext):
        pass

    # Exit a parse tree produced by pascalParser#forList.
    def exitForList(self, ctx: pascalParser.ForListContext):
        pass

    # Enter a parse tree produced by pascalParser#initialValue.
    def enterInitialValue(self, ctx: pascalParser.InitialValueContext):
        pass

    # Exit a parse tree produced by pascalParser#initialValue.
    def exitInitialValue(self, ctx: pascalParser.InitialValueContext):
        pass

    # Enter a parse tree produced by pascalParser#finalValue.
    def enterFinalValue(self, ctx: pascalParser.FinalValueContext):
        pass

    # Exit a parse tree produced by pascalParser#finalValue.
    def exitFinalValue(self, ctx: pascalParser.FinalValueContext):
        pass

    # Enter a parse tree produced by pascalParser#withStatement.
    def enterWithStatement(self, ctx: pascalParser.WithStatementContext):
        pass

    # Exit a parse tree produced by pascalParser#withStatement.
    def exitWithStatement(self, ctx: pascalParser.WithStatementContext):
        pass

    # Enter a parse tree produced by pascalParser#recordVariableList.
    def enterRecordVariableList(self, ctx: pascalParser.RecordVariableListContext):
        pass

    # Exit a parse tree produced by pascalParser#recordVariableList.
    def exitRecordVariableList(self, ctx: pascalParser.RecordVariableListContext):
        pass

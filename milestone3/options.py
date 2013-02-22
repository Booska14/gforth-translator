

optionParseAll = "-a"
optionParseAllDef = "let the parser go through all files even if an error is found"

optionTokenizeAll = "-z"
optionTokenizeAllDef = "let the tokenizer go through all file even if an error is found"

optionhelp = "-h"
optionhelpDef = "Get usage and list of options for program"

optionPrintTokens = "-t"
optionPrintTokensDef = "print out the tokens for all files"

optionPrintProductionRules = "-r"
optionPrintProductionRulesDef = "Print out the prodcution rules use for each token"

optionList = dict([(optionParseAll, optionParseAllDef), (optionhelp, optionhelpDef), (optionPrintTokens, optionPrintTokensDef), (optionPrintProductionRules,optionPrintProductionRulesDef), (optionTokenizeAll, optionTokenizeAllDef)])

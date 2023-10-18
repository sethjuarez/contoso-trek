param (
    [Parameter(Mandatory=$true)]
    [string]$name
)
pf run create --flow ./eval/groundedness --data ./data/testdata.jsonl --column-mapping question='${data.question}' context='${run.outputs.context}' answer='${run.outputs.answer}' --run $name --stream

# pf run show-details --name run name
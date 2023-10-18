param (
    [Parameter(Mandatory=$true)]
    [string]$name
)
pf run create --flow . --data ./data/testdata.jsonl --column-mapping customerId='${data.customerId}' question='${data.question}' chat_history='${data.chat_history}' --name $name --stream 


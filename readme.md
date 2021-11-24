### Criar arquivo zip para deploy da função Lambda
Para criar o arquivo zip com todo o código necessário para executar a aplicação no ambiente do AWS Lambda, basta executar script build.sh (ambiente Unix):

```bash
./build.sh
```

Ao final da execução, um arquivo build.zip será criado dentro da pasta build.

### Executar script do terraform

Pré-requisitos:
* ter o Terraform instalado (https://learn.hashicorp.com/tutorials/terraform/install-cli)
* ter o AWS CLI instalado (https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
* ter um profile default configurado no AWS CLI com permissões para criar os componentes do script (https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html)
* ter gerado arquivo build.zip dentro da pasta build (descrito no tópico acima)

Comandos para iniciar e executar o terraform:
```bash
cd terraform
terraform init
terraform plan
terraform apply
```
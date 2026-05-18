const toolDescriptions = {
  "Copilot Chat": "Assistente de chat para programadores integrado ao editor",
  "Copilot CLI":
    "Ferramenta para gerar comandos de terminal a partir de descricoes",
  "Copilot Labs":
    "Conjunto experimental de funcionalidades adicionais do Copilot",
};

const toolName = gets();


if (toolDescriptions[toolName]) {
  console.log(toolDescriptions[toolName]);
} else {
  console.log("ferramenta nao encontrada");
}

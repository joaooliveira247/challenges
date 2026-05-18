const techniqueDescriptions = {
  "zero shot": "Prompt sem exemplos, modelo infere a tarefa diretamente",
  "few shot": "Prompt com poucos exemplos para orientar o modelo",
  "chain of thought": "Prompt que incentiva o modelo a explicar o raciocinio",
  "role prompting":
    "Prompt define o papel ou comportamento esperado do modelo",
};

const technique = gets();

if (techniqueDescriptions[technique]) {
  console.log(techniqueDescriptions[technique]);
} else {
  console.log("Technique not recognized");
}

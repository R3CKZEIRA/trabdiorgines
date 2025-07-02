import tkinter as tk
from tkinter import ttk, messagebox
import random

class SistemaBuscaSequencial:
    def __init__(self, janela_principal):
        self.janela_principal = janela_principal
        self.janela_principal.title("Sistema de Busca Sequencial")
        self.janela_principal.geometry("900x700")
        self.janela_principal.configure(bg='#f0f0f0')
        
        # Lista para armazenar os elementos
        self.lista_elementos = []
        
        self.criar_interface()
    
    def criar_interface(self):
        # Título
        titulo = tk.Label(
            self.janela_principal, 
            text="Sistema de Busca Sequencial do Diorgines", 
            font=("Arial", 16, "bold"),
            bg='#f0f0f0',
            fg='#333'
        )
        titulo.pack(pady=10)
        
        # Frame para entrada da lista
        frame_lista = tk.Frame(self.janela_principal, bg='#f0f0f0')
        frame_lista.pack(pady=10, padx=20, fill='x')
        
        tk.Label(
            frame_lista, 
            text="Digite os elementos da lista (separados por vírgula se for mais de um):",
            bg='#f0f0f0',
            font=("Arial", 12)
        ).pack(anchor='w')
        
        self.entrada_lista = tk.Entry(frame_lista, font=("Arial", 12), width=80)
        self.entrada_lista.pack(pady=5, fill='x')
        
        # Botões para gerar listas
        frame_botoes_lista = tk.Frame(self.janela_principal, bg='#f0f0f0')
        frame_botoes_lista.pack(pady=5)
        
        btn_lista_aleatoria = tk.Button(
            frame_botoes_lista,
            text="Gerar Lista Aleatória",
            command=self.gerar_lista_aleatoria,
            bg='#4CAF50',
            fg='white',
            font=("Arial", 12)
        )
        btn_lista_aleatoria.pack(side='left', padx=5)
        
        btn_lista_ordenada = tk.Button(
            frame_botoes_lista,
            text="Gerar Lista Ordenada",
            command=self.gerar_lista_ordenada,
            bg='#2196F3',
            fg='white',
            font=("Arial", 12)
        )
        btn_lista_ordenada.pack(side='left', padx=5)
        
        # Frame para valor a ser buscado
        frame_busca = tk.Frame(self.janela_principal, bg='#f0f0f0')
        frame_busca.pack(pady=10, padx=20, fill='x')
        
        tk.Label(
            frame_busca, 
            text="Digite o valor a ser buscado:",
            bg='#f0f0f0',
            font=("Arial", 12)
        ).pack(anchor='w')
        
        self.entrada_valor_busca = tk.Entry(frame_busca, font=("Arial", 12), width=30)
        self.entrada_valor_busca.pack(pady=5, anchor='w')
        
        # Botão de busca
        btn_buscar = tk.Button(
            self.janela_principal,
            text="Realizar Busca Sequencial",
            command=self.realizar_busca,
            bg='#FF9800',
            fg='white',
            font=("Arial", 12, "bold"),
            pady=10
        )
        btn_buscar.pack(pady=15)
        
        # Área de resultados
        frame_resultados = tk.Frame(self.janela_principal, bg='#f0f0f0')
        frame_resultados.pack(pady=10, padx=20, fill='both', expand=True)
        
        tk.Label(
            frame_resultados, 
            text="Resultados:",
            bg='#f0f0f0',
            font=("Arial", 12, "bold")
        ).pack(anchor='w')
        
        self.texto_resultados = tk.Text(
            frame_resultados, 
            height=18, 
            width=100,
            font=("Courier", 11),
            bg='white',
            relief='sunken',
            borderwidth=2
        )
        self.texto_resultados.pack(pady=5, fill='both', expand=True)
        
        # Scrollbar para o texto de resultados
        scrollbar = tk.Scrollbar(self.texto_resultados)
        scrollbar.pack(side='right', fill='y')
        self.texto_resultados.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.texto_resultados.yview)
    
    def gerar_lista_aleatoria(self):
        """Gera uma lista aleatória de números"""
        numeros_aleatorios = [random.randint(1, 100) for _ in range(15)]
        lista_texto = ', '.join(map(str, numeros_aleatorios))
        self.entrada_lista.delete(0, tk.END)
        self.entrada_lista.insert(0, lista_texto)
    
    def gerar_lista_ordenada(self):
        """Gera uma lista ordenada de números"""
        numeros_ordenados = sorted([random.randint(1, 100) for _ in range(15)])
        lista_texto = ', '.join(map(str, numeros_ordenados))
        self.entrada_lista.delete(0, tk.END)
        self.entrada_lista.insert(0, lista_texto)
    
    def busca_sequencial(self, lista_elementos, valor_procurado):
        """
        Implementa o algoritmo de busca sequencial
        Retorna: (posicao_encontrada, numero_comparacoes, detalhes_busca)
        """
        numero_comparacoes = 0
        detalhes_busca = []
        
        detalhes_busca.append(f"Iniciando busca sequencial por: {valor_procurado}")
        detalhes_busca.append(f"Lista: {lista_elementos}")
        detalhes_busca.append("-" * 50)
        
        for indice in range(len(lista_elementos)):
            numero_comparacoes += 1
            elemento_atual = lista_elementos[indice]
            
            detalhes_busca.append(
                f"Comparação {numero_comparacoes}: "
                f"Posição {indice} -> {elemento_atual} == {valor_procurado}?"
            )
            
            if elemento_atual == valor_procurado:
                detalhes_busca.append(f"✓ ACHEI C****** estava na posição {indice}!")
                return indice, numero_comparacoes, detalhes_busca
            else:
                detalhes_busca.append("✗ Não achei aqui senhoras e senhores...")
        
        detalhes_busca.append("✗ Lamento, não encontrei esse número seu m****")
        return -1, numero_comparacoes, detalhes_busca
    
    def realizar_busca(self):
        """Executa a busca sequencial e exibe os resultados"""
        try:
            # Obter e processar a lista de elementos
            texto_lista = self.entrada_lista.get().strip()
            if not texto_lista:
                messagebox.showerror("Erro", "Amigo, Por favor, insira uma lista de elementos senão não tem o que procurar!")
                return
            
            # Converter string para lista de números
            self.lista_elementos = [int(x.strip()) for x in texto_lista.split(',')]
            
            # Obter valor a ser buscado
            texto_valor = self.entrada_valor_busca.get().strip()
            if not texto_valor:
                messagebox.showerror("Erro", "Amigo, me ajuda a te ajudar, insira um número para pesquisar!")
                return
            
            valor_procurado = int(texto_valor)
            
            # Realizar busca sequencial
            posicao_encontrada, numero_comparacoes, detalhes_busca = self.busca_sequencial(
                self.lista_elementos, valor_procurado
            )
            
            # Limpar área de resultados
            self.texto_resultados.delete(1.0, tk.END)
            
            # Exibir resultados
            resultado_texto = "\n".join(detalhes_busca)
            resultado_texto += "\n" + "=" * 50
            resultado_texto += f"\nRESUMO DA BUSCA:"
            resultado_texto += f"\nValor buscado: {valor_procurado}"
            resultado_texto += f"\nTamanho da lista: {len(self.lista_elementos)} elementos"
            resultado_texto += f"\nNúmero de comparações: {numero_comparacoes}"
            
            if posicao_encontrada != -1:
                resultado_texto += f"\nResultado: ENCONTRADO na posição {posicao_encontrada}"
                resultado_texto += f"\nÍndice (base 0): {posicao_encontrada}"
                resultado_texto += f"\nPosição (base 1): {posicao_encontrada + 1}"
            else:
                resultado_texto += f"\nResultado: NÃO ENCONTRADO"
            
            # Análise de eficiência
            resultado_texto += f"\n\nANÁLISE DE EFICIÊNCIA:"
            porcentagem_lista = (numero_comparacoes / len(self.lista_elementos)) * 100
            resultado_texto += f"\nPercentual da lista percorrido: {porcentagem_lista:.1f}%"
            
            if posicao_encontrada != -1:
                if numero_comparacoes == 1:
                    resultado_texto += "\nEficiência: ÓTIMA (encontrado na primeira posição)"
                elif numero_comparacoes <= len(self.lista_elementos) // 2:
                    resultado_texto += "\nEficiência: BOA (encontrado na primeira metade)"
                else:
                    resultado_texto += "\nEficiência: REGULAR (encontrado na segunda metade)"
            else:
                resultado_texto += "\nEficiência: PIOR CASO (percorreu toda a lista)"
            
            self.texto_resultados.insert(tk.END, resultado_texto)
            
        except ValueError:
            messagebox.showerror(
                "Erro", 
                "Por favor amigo, insira apenas números válidos separados por vírgula!"
            )
        except Exception as erro:
            messagebox.showerror("Erro", f"Ocorreu um erro: {str(erro)}")

def main():
    """Função principal para executar o sistema"""
    janela_principal = tk.Tk()
    aplicacao = SistemaBuscaSequencial(janela_principal)
    janela_principal.mainloop()

if __name__ == "__main__":
    main()

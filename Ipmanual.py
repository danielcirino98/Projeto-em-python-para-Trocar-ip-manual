import tkinter as tk #importação do pacote Tkinter




ipv4 = ['192.168.0.102', '192.168.0.103', '192.168.0.104', '192.168.0.105',  #Minha variavel com Ips estáticos
        '192.168.0.106', '192.168.0.107', '192.168.0.108', '192.168.0.109', 
        '192.168.0.110', '192.168.0.111', '192.168.0.112', '192.168.0.113', 
        '192.168.0.114', '192.168.0.115', '192.168.0.116', '192.168.0.117', '192.168.0.118', '192.168.0.119', 
        '192.168.0.106', '192.168.0.107', '192.168.0.108', '192.168.0.109', 
        '192.168.0.120', '192.168.0.121', '192.168.0.122', '192.168.0.123', 
        '192.168.0.124', '192.168.0.125', '192.168.0.126', '192.168.0.127', '192.168.0.128', '192.168.0.129', 
        '192.168.0.130', '192.168.0.131', '192.168.0.132', '192.168.0.133', 
        '192.168.0.134', '192.168.0.135', '192.168.0.136', '192.168.0.137', 
        '192.168.0.138', '192.168.0.139' '192.168.0.1', '192.168.0.2', '192.168.0.3', '192.168.0.4', 
        '192.168.0.5', '192.168.0.6', '192.168.0.7', '192.168.0.7', 
        '192.168.0.8', '192.168.0.9', '192.168.0.10', '192.168.0.11', 
        '192.168.0.12', '192.168.0.13', '192.168.0.14', '192.168.0.115', '192.168.0.16', '192.168.0.17', 
        '192.168.0.18', '192.168.0.19', '192.168.0.20', '192.168.0.21', 
        '192.168.0.22', '192.168.0.23', '192.168.0.124', '192.168.0.25', 
        '192.168.0.26', '192.168.0.27', '192.168.0.28', '192.168.0.29', '192.168.0.30', '192.168.0.31', 
        '192.168.0.32', '192.168.0.33', '192.168.0.34', '192.168.0.35', 
        '192.168.0.36', '192.168.0.37', '192.168.0.38', '192.168.0.39', 
        '192.168.0.40', '192.168.0.41']

dns = ["DNS Primário google: 8.8.8.8 DNS Secundário google: 8.8.4.4\nDNS Primário cloudflare:  1.1.1.1 DNS Secundário cloudflare: 1.0.0.1 gateway padrão: 192.168.0.1 Comprimento do prefixo de rede: 24/"] #Minha variável de DNS
def capturar_dados(): # Minha função que retorna um mensagem em caixa popup
    entrada = int(entry.get())# Pega os dados de entrada
    if entrada >= 0 and entrada <= 100: #verifica se existe o número total da lista(reatorna  uma mensagem)
        messagebox.showinfo("Dados Capturados", f"Seu novo Ip: {ipv4[entrada],[dns]}")
    else:
        messagebox.showwarning("Aviso", "Número inválido!")


root = tk.Tk() # ìnicio da interface gráfica
root.geometry("300x150") # Tamanoa de Tela da interface(Ajustável)
root.title("IpManual")

label = tk.Label(root, text="Digite de 0 - 82:\n Veja qual Ip Deves usar!")
label.pack(pady=10)

entry = tk.Entry(root, width=30)
entry.pack(pady=5)

botao = tk.Button(root, text="Enviar", command=capturar_dados)
botao.pack(pady=10,)



#mostrar = tk.Label(root, text= "@cirinotech")
#50% IA 50% Humano
#mostrar.pack(pady=10, padx=55)



from tkinter import messagebox

root.mainloop()

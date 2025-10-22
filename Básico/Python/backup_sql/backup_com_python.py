import sqlite3

# Abre o banco de origem e o de destino (backup)
src_conn = sqlite3.connect("C:\\Users\\999532\\OneDrive - SENAC em Minas - EDU\\T.I\\backup_sql\\meu_banco.db")
dest_conn = sqlite3.connect("C:\\Users\\999532\\OneDrive - SENAC em Minas - EDU\\T.I\\backup_sql\\backup_banco.db")

# Iniciar
with dest_conn:
    src_conn.backup(dest_conn)

# Fechar 
src_conn.close()
dest_conn.close()

print("Backup feito!")

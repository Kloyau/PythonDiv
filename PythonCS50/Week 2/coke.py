def main():
    m_i=0
    m_d=50
    i_coin = 0
    while m_d > m_i:
        print(f"Amount Due: {m_d-m_i}")
        i_coin=int(input())
        if i_coin in [25,10,5]:
            m_i+=i_coin
    print(f"Change Owed: {m_i-m_d}")

main()

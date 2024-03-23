def add_liquidity(
    self,
    token_a: str,
    token_b: str,
    amount_a: str,
    amount_b: str,
    min_amount_a: str,
    min_amount_b: str,
    max_price: str,
    min_price: str,
    deadline: int,
    sender: str,
    receiver: str,
    approval_amount: str,
    fee: int,
    nonce: int,
    chain_id: int,
    gas_price: int,
    gas_limit: int,
) -> TransactionReceipt:
    """Add liquidity to a pool.

    Args:
        token_a (str): Address of the first token.
        token_b (str): Address of the second token.
        amount_a (str): Amount of the first token to add.
        amount_b (str): Amount of the second token to add.
        min_amount_a (str): Minimum amount of the first token to add.
        min_amount_b (str): Minimum amount of the second token to add.
        max_price (str): Maximum price of the first token in terms of the second token.
        min_price (str): Minimum price of the first token in terms of the second token.
        deadline (int): Deadline for the transaction to be valid.
        sender (str): Address of the sender.
        receiver (str): Address of the receiver.
        approval_amount (str): Amount of the first token to approve.
        fee (int): Fee for the transaction.
        nonce (int): Nonce for the transaction.
        chain_id (int): Chain ID for the transaction.
        gas_price (int): Gas price for the transaction.
        gas_limit (int): Gas limit for the transaction.

    Returns:
        TransactionReceipt: Transaction receipt.
    """

    if not isinstance(token_a, str):
        raise TypeError("token_a must be a string")
    if not isinstance(token_b, str):
        raise TypeError("token_b must be a string")
    if not isinstance(amount_a, str):
        raise TypeError("amount_a must be a string")
    if not isinstance(amount_b, str):
        raise TypeError("amount_b must be a string")
    if not isinstance(min_amount_a, str):
        raise TypeError("min_amount_a must be a string")
    if not isinstance(min_amount_b, str):
        raise TypeError("min_amount_b must be a string")
    if not isinstance(max_price, str):
        raise TypeError("max_price must be a string")
    if not isinstance(min_price, str):
        raise TypeError("min_price must be a string")
    if not isinstance(deadline, int):
        raise TypeError("deadline must be an integer")
    if not isinstance(sender, str):
        raise TypeError("sender must be a string")
    if not isinstance(receiver, str):
        raise TypeError("receiver must be a string")
    if not isinstance(approval_amount, str):
        raise TypeError("approval_amount must be a string")
    if not isinstance(fee, int):
        raise TypeError("fee must be an integer")
    if not isinstance(nonce, int):
        raise TypeError("nonce must be an integer")
    if not isinstance(chain_id, int):
        raise TypeError("chain_id must be an integer")
    if not isinstance(gas_price, int):
        raise TypeError("gas_price must be an integer")
    if not isinstance(gas_limit, int):
        raise TypeError("gas_limit must be an integer")

    hop_contract = self.get_hop_contract()
    hop_contract.functions.addLiquidity(
        token_a,
        token_b,
        amount_a,
        amount_b,
        min_amount_a,
        min_amount_b,
        max_price,
        min_price,
        deadline,
        sender,
        receiver,
        approval_amount,
        fee,
        nonce,
    ).transact(
        {
            "from": sender,
            "gas_price": gas_price,
            "gas": gas_limit,
            "chain_id": chain_id,
        }
    )

    transaction_receipt = self.w3.eth.wait_for_transaction_receipt(
        hop_contract.functions.addLiquidity(
            token_a,
            token_b,
            amount_a,
            amount_b,
            min_amount_a,
            min_amount_b,
            max_price,
            min_price,
            deadline,
            sender,
            receiver,
            approval_amount,
            fee,
            nonce,
        ).transact(
            {
                "from": sender,
                "gas_price": gas_price,
                "gas": gas_limit,
                "chain_id": chain_id,
            }
        ).txid
    )

    cprint(f'\n>>> HOP add_liquidity | {transaction_receipt.status}', 'green')

    return transaction_receipt


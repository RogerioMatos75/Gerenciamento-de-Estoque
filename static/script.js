document.addEventListener('DOMContentLoaded', () => {
    const productForm = document.getElementById('add-product-form');
    const productList = document.getElementById('product-list');
    const stockControlForm = document.getElementById('stock-control-form');
    const stockProductIdInput = document.getElementById('stock_product_id');
    const stockQuantityInput = document.getElementById('stock_quantity');
    const btnEntrada = document.getElementById('btn-entrada');
    const btnSaida = document.getElementById('btn-saida');

    const API_URL = '/produtos';

    // Função para buscar e renderizar os produtos
    async function fetchProducts() {
        try {
            const response = await fetch(API_URL);
            if (!response.ok) {
                throw new Error('Erro ao buscar produtos.');
            }
            const products = await response.json();

            productList.innerHTML = ''; // Limpa a lista atual

            products.forEach(product => {
                const tr = document.createElement('tr');
                tr.innerHTML = `
                    <td>${product.id}</td>
                    <td>${product.nome}</td>
                    <td>${product.categoria}</td>
                    <td>R$ ${product.preco.toFixed(2)}</td>
                    <td>${product.quantidade}</td>
                    <td>${product.estoque_minimo}</td>
                    <td>
                        <button class="btn-details" data-id="${product.id}">Detalhes</button>
                    </td>
                    <td>
                        ${product.alert_message ? `<span class="alert-message">${product.alert_message}</span>` : ''}
                    </td>
                `;
                productList.appendChild(tr);
            });
        } catch (error) {
            console.error('Erro:', error);
            productList.innerHTML = '<tr><td colspan="8">Falha ao carregar produtos.</td></tr>';
        }
    }

    // Função para buscar e mostrar detalhes de um produto
    async function showProductDetails(id) {
        try {
            const response = await fetch(`${API_URL}/${id}`);
            if (!response.ok) {
                throw new Error(`Produto com ID ${id} não encontrado.`);
            }
            const product = await response.json();

            // Formata os detalhes para exibição no alert
            const details = `
                Detalhes do Produto:
                --------------------------
                ID: ${product.id}
                Nome: ${product.nome}
                Categoria: ${product.categoria}
                Preço: R$ ${product.preco.toFixed(2)}
                Quantidade: ${product.quantidade}
                Estoque Mínimo: ${product.estoque_minimo}
                ${product.alert_message ? `\nAlerta: ${product.alert_message}` : ''}
            `;
            alert(details);
        } catch (error) {
            console.error('Erro:', error);
            alert(error.message);
        }
    }
    
    // Função para adicionar um novo produto
    async function addProduct(event) {
        event.preventDefault(); 

        const formData = new FormData(productForm);
        const productData = {
            nome: formData.get('nome'),
            categoria: formData.get('categoria'),
            preco: parseFloat(formData.get('preco')),
            quantidade: parseInt(formData.get('quantidade'), 10),
            estoque_minimo: parseInt(formData.get('estoque_minimo'), 10)
        };

        try {
            const response = await fetch(API_URL, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(productData)
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || 'Erro ao adicionar produto.');
            }

            productForm.reset();
            await fetchProducts();

            const lastRow = productList.lastElementChild;
            if (lastRow) {
                lastRow.classList.add('flash-new-row');
            }

        } catch (error) {
            console.error('Erro:', error);
            alert(error.message);
        }
    }

    // Função para controlar entrada/saída de estoque
    async function handleStockMovement(type) {
        const productId = parseInt(stockProductIdInput.value, 10);
        const quantity = parseInt(stockQuantityInput.value, 10);

        if (isNaN(productId) || productId <= 0) {
            alert("Por favor, insira um ID de produto válido.");
            return;
        }
        if (isNaN(quantity) || quantity <= 0) {
            alert("Por favor, insira uma quantidade válida (maior que zero).");
            return;
        }

        try {
            const response = await fetch(`${API_URL}/${productId}/${type}`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ quantidade: quantity })
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || `Erro ao registrar ${type}.`);
            }

            stockControlForm.reset();
            await fetchProducts();
            alert(`Movimentação de ${type} registrada com sucesso para o produto ID ${productId}!`);

        } catch (error) {
            console.error('Erro:', error);
            alert(error.message);
        }
    }

    // Adiciona os event listeners
    productForm.addEventListener('submit', addProduct);
    productList.addEventListener('click', (event) => {
        if (event.target && event.target.classList.contains('btn-details')) {
            const productId = event.target.getAttribute('data-id');
            showProductDetails(productId);
        }
    });
    btnEntrada.addEventListener('click', () => handleStockMovement('entrada'));
    btnSaida.addEventListener('click', () => handleStockMovement('saida'));

    // Carrega os produtos ao iniciar a página
    fetchProducts();
});

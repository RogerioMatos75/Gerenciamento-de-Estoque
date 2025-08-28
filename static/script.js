document.addEventListener('DOMContentLoaded', () => {
    // --- Elementos do DOM ---
    const productForm = document.getElementById('add-product-form');
    const productList = document.getElementById('product-list');
    const stockControlForm = document.getElementById('stock-control-form');
    const stockProductIdInput = document.getElementById('stock_product_id');
    const stockQuantityInput = document.getElementById('stock_quantity');
    const btnEntrada = document.getElementById('btn-entrada');
    const btnSaida = document.getElementById('btn-saida');
    const formTitle = document.querySelector('#add-product-form').parentElement.querySelector('h2');
    const submitButton = productForm.querySelector('button[type="submit"]');
    const filterNomeInput = document.getElementById('filter-nome');
    const filterCategoriaInput = document.getElementById('filter-categoria');
    const btnBaixoEstoque = document.getElementById('btn-baixo-estoque');
    const btnVerTodos = document.getElementById('btn-ver-todos');

    // --- Estado e Configuração ---
    const API_URL = '/produtos';
    let currentEditId = null;
    let debounceTimer;

    // --- Funções Utilitárias ---
    function debounce(func, delay) {
        clearTimeout(debounceTimer);
        debounceTimer = setTimeout(func, delay);
    }

    // --- Funções de Renderização e API ---

    async function renderProductTable(requestUrl) {
        try {
            const response = await fetch(requestUrl);
            if (!response.ok) throw new Error('Erro ao buscar dados dos produtos.');
            const products = await response.json();

            productList.innerHTML = '';

            if (products.length === 0) {
                productList.innerHTML = '<tr><td colspan="8" style="text-align: center;">Nenhum produto encontrado.</td></tr>';
                return;
            }

            products.forEach(product => {
                const tr = document.createElement('tr');
                tr.dataset.productId = product.id;
                tr.innerHTML = `
                    <td>${product.id}</td>
                    <td>${product.nome}</td>
                    <td>${product.categoria}</td>
                    <td>R$ ${product.preco.toFixed(2)}</td>
                    <td>${product.quantidade}</td>
                    <td>${product.estoque_minimo}</td>
                    <td class="actions">
                        <button class="btn-edit" data-id="${product.id}">Editar</button>
                        <button class="btn-details" data-id="${product.id}">Detalhes</button>
                        <button class="btn-remove" data-id="${product.id}">Remover</button>
                    </td>
                    <td>
                        ${product.alert_message ? `<span class="alert-message">${product.alert_message}</span>` : ''}
                    </td>
                `;
                productList.appendChild(tr);
            });
        } catch (error) {
            console.error('Erro:', error);
            productList.innerHTML = '<tr><td colspan="8" style="text-align: center;">Falha ao carregar produtos.</td></tr>';
        }
    }

    function fetchAndFilterProducts() {
        const nomeFilter = filterNomeInput.value.trim();
        const categoriaFilter = filterCategoriaInput.value.trim();
        const params = new URLSearchParams();
        if (nomeFilter) params.append('nome', nomeFilter);
        if (categoriaFilter) params.append('categoria', categoriaFilter);
        const queryString = params.toString();
        const requestUrl = queryString ? `${API_URL}?${queryString}` : API_URL;
        renderProductTable(requestUrl);
    }

    function setEditMode(product) {
        currentEditId = product.id;
        formTitle.textContent = `Editando Produto ID: ${product.id}`;
        productForm.nome.value = product.nome;
        productForm.categoria.value = product.categoria;
        productForm.preco.value = product.preco;
        productForm.quantidade.value = product.quantidade;
        productForm.estoque_minimo.value = product.estoque_minimo;
        submitButton.textContent = 'Atualizar Produto';
        if (!productForm.querySelector('.btn-cancel')) {
            const cancelButton = document.createElement('button');
            cancelButton.type = 'button';
            cancelButton.textContent = 'Cancelar Edição';
            cancelButton.classList.add('btn', 'btn-cancel');
            submitButton.insertAdjacentElement('afterend', cancelButton);
            cancelButton.addEventListener('click', cancelEditMode);
        }
        productForm.scrollIntoView({ behavior: 'smooth' });
    }

    function cancelEditMode() {
        currentEditId = null;
        formTitle.textContent = 'Adicionar Novo Produto';
        submitButton.textContent = 'Salvar Produto';
        productForm.reset();
        const cancelButton = productForm.querySelector('.btn-cancel');
        if (cancelButton) cancelButton.remove();
    }

    async function showProductDetails(id) {
        try {
            const response = await fetch(`${API_URL}/${id}`);
            if (!response.ok) throw new Error(`Produto com ID ${id} não encontrado.`);
            const product = await response.json();
            const details = `
                Detalhes do Produto:\n                --------------------------\n                ID: ${product.id}\n                Nome: ${product.nome}\n                Categoria: ${product.categoria}\n                Preço: R$ ${product.preco.toFixed(2)}\n                Quantidade: ${product.quantidade}\n                Estoque Mínimo: ${product.estoque_minimo}
                ${product.alert_message ? `\nAlerta: ${product.alert_message}` : ''}
            `;
            alert(details);
        } catch (error) {
            console.error('Erro:', error);
            alert(error.message);
        }
    }

    async function startEdit(id) {
        try {
            const response = await fetch(`${API_URL}/${id}`);
            if (!response.ok) throw new Error(`Produto com ID ${id} não encontrado.`);
            const product = await response.json();
            setEditMode(product);
        } catch (error) {
            console.error('Erro:', error);
            alert(error.message);
        }
    }

    async function handleFormSubmit(event) {
        event.preventDefault();
        const formData = new FormData(productForm);
        const productData = {
            nome: formData.get('nome'),
            categoria: formData.get('categoria'),
            preco: parseFloat(formData.get('preco')),
            quantidade: parseInt(formData.get('quantidade'), 10),
            estoque_minimo: parseInt(formData.get('estoque_minimo'), 10)
        };
        const url = currentEditId ? `${API_URL}/${currentEditId}` : API_URL;
        const method = currentEditId ? 'PUT' : 'POST';
        try {
            const response = await fetch(url, {
                method: method,
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(productData)
            });
            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || 'Erro ao salvar produto.');
            }
            let newOrUpdatedId = currentEditId;
            if (method === 'POST') {
                const newProduct = await response.json();
                newOrUpdatedId = newProduct.id;
            }
            cancelEditMode();
            await fetchAndFilterProducts();
            if (newOrUpdatedId) {
                const updatedRow = productList.querySelector(`[data-product-id="${newOrUpdatedId}"]`);
                if(updatedRow) updatedRow.classList.add('flash-new-row');
            }
        } catch (error) {
            console.error('Erro:', error);
            alert(error.message);
        }
    }

    async function handleStockMovement(type) {
        const productId = parseInt(stockProductIdInput.value, 10);
        const quantity = parseInt(stockQuantityInput.value, 10);
        if (isNaN(productId) || isNaN(quantity) || quantity <= 0) {
            alert("Por favor, insira um ID e uma quantidade válidos.");
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
            await fetchAndFilterProducts();
            alert(`Movimentação de ${type} registrada com sucesso!`);
        } catch (error) {
            console.error('Erro:', error);
            alert(error.message);
        }
    }

    async function removeProduct(id) {
        if (!confirm(`Tem certeza que deseja remover o produto com ID ${id}?`)) return;
        try {
            const response = await fetch(`${API_URL}/${id}`, { method: 'DELETE' });
            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || 'Erro ao remover produto.');
            }
            await fetchAndFilterProducts();
            alert(`Produto com ID ${id} removido com sucesso!`);
        } catch (error) {
            console.error('Erro:', error);
            alert(error.message);
        }
    }

    // --- Adiciona os Event Listeners ---
    productForm.addEventListener('submit', handleFormSubmit);

    productList.addEventListener('click', (event) => {
        const target = event.target;
        if (target.classList.contains('btn-details')) {
            showProductDetails(target.dataset.id);
        } else if (target.classList.contains('btn-remove')) {
            removeProduct(target.dataset.id);
        } else if (target.classList.contains('btn-edit')) {
            startEdit(target.dataset.id);
        }
    });

    btnEntrada.addEventListener('click', () => handleStockMovement('entrada'));
    btnSaida.addEventListener('click', () => handleStockMovement('saida'));

    filterNomeInput.addEventListener('input', () => debounce(fetchAndFilterProducts, 300));
    filterCategoriaInput.addEventListener('input', () => debounce(fetchAndFilterProducts, 300));

    btnBaixoEstoque.addEventListener('click', () => {
        renderProductTable(`${API_URL}/baixo-estoque`);
        btnBaixoEstoque.classList.add('hidden');
        btnVerTodos.classList.remove('hidden');
    });

    btnVerTodos.addEventListener('click', () => {
        fetchAndFilterProducts();
        btnVerTodos.classList.add('hidden');
        btnBaixoEstoque.classList.remove('hidden');
    });

    // Carrega os produtos ao iniciar a página
    fetchAndFilterProducts();
});